import re
import datetime
from fastapi import HTTPException
from model.user import User
from db.Warehouse import Warehouse

class UserController:
    def __init__(self):
        self.__users_db = Warehouse(('127.0.0.1', 8100))
        self.__users_db.connect()
    
    async def create_user(self,request, body):
        try:
            new_user = self.validate_user(body)
            saved_user = self.__users_db.create(new_user)
            return {"message": "User created successfully", "user": saved_user}
        except HTTPException as http_e:
            raise http_e
        except Exception as e:
            print("Exception:", e)  
            raise HTTPException(status_code=500, detail="Internal Server Error")

    async def get_users(self,request):
        try:
            users = self.__users_db.findAll()
            users = [user for user in users if isinstance(user, User)]
            return users
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    async def get_user(self,request, user_id):
        try:
            user = self.__users_db.findOne(user_id)
            if isinstance(user, User):
                return user
            else:
                raise HTTPException(status_code=404, detail="User not found")
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    async def update_user(self,request, user_id, body):
        try:
            user = self.__users_db.findOne(user_id)
            if isinstance(user, User):
                updated_user = User(
                    body.get("name", user.name),
                    body.get("birthDate", user.birthDate),
                    body.get("citizenID", user.citizenID),
                    body.get("phoneNumber", user.phoneNumber),
                    body.get("email", user.email),
                    body.get("username", user.username),
                    body.get("password", user.password),
                )
                user = self.__users_db.findOneAndUpdate(user_id, updated_user)
                return user
            else:
                raise HTTPException(status_code=404, detail="User not found")
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    async def delete_user(self, request, user_id):
        try:
            deleted_user = self.__users_db.findOneAndDelete(user_id)
            if deleted_user:
                return {"message": "User deleted successfully"}
            else:
                raise HTTPException(status_code=404, detail="User not found")
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    async def add_user_photo(self, request, user_id, body):
        try:
            user = self.__users_db.findOne(user_id)
            if isinstance(user, User):
                user.addPicture(body["photoURL"])
                updated_user = self.__users_db.findOneAndUpdate(user_id, user)
                return updated_user
            else:
                raise HTTPException(status_code=404, detail="User not found")
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    def validate_user(self, body):
        try:
            new_user = User(
                self.validate_name(body.get("name", "")),
                self.validate_date_of_birth(body.get("birthDate", "")),
                self.validate_citizen_id(body.get("citizenID", "")),
                self.validate_phone_number(body.get("phoneNumber", "")),
                self.validate_email(body.get("email", "")),
                self.validate_username(body.get("username", "")),
                self.validate_password(body.get("password", "")),
            )
            
            users = [user for user in self.__users_db.findAll() if isinstance(user, User)]
            for user in users:
                if user.email == new_user.email:
                    raise HTTPException(status_code=400, detail="Email already exists")
                if user.username == new_user.username:
                    raise HTTPException(status_code=400, detail="Username already exists")
            print(new_user)
            return new_user
        except HTTPException as http_e:
            raise http_e
        except Exception as e:
            print("Exception:", e)  
            raise HTTPException(status_code=500, detail="Internal Server Error")
    
    def validate_name(self, name):
        if not name:
            raise HTTPException(status_code=400, detail="Name is required")
        if len(name) < 2:
            raise HTTPException(status_code=400, detail="Name must be at least 2 characters long")
        return name.strip()

    def validate_date_of_birth(self, birth_date):
        if not birth_date:
            return None
        try:
            datetime.datetime.strptime(birth_date, "%Y-%m-%d")
            return birth_date
        except ValueError:
            raise HTTPException(status_code=400, detail="Invalid date of birth format. Use YYYY-MM-DD")

    def validate_citizen_id(self, citizen_id):
        if not citizen_id:
            raise HTTPException(status_code=400, detail="Citizen ID is required")
        if type(citizen_id) != int:
            raise HTTPException(status_code=400, detail="Citizen ID must contain only digits")
        if len(str(citizen_id)) != 13:
            raise HTTPException(status_code=400, detail="Citizen ID must be 13 digits long")
        return citizen_id

    def validate_phone_number(self, phone_number):
        if not phone_number:
            return None
        if type(phone_number) != int:
            raise HTTPException(status_code=400, detail="Phone number must contain only digits")
        if len(str(phone_number)) != 10:
            raise HTTPException(status_code=400, detail="Phone number must be 10 digits long")
        return phone_number

    def validate_email(self, email):
        if not email:
            raise HTTPException(status_code=400, detail="Email is required")
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            raise HTTPException(status_code=400, detail="Invalid email format")
        return email.strip()

    def validate_username(self, username):
        if not username:
            raise HTTPException(status_code=400, detail="Username is required")
        if len(username) < 5:
            raise HTTPException(status_code=400, detail="Username must be at least 5 characters long")
        return username.strip()

    def validate_password(self, password):
        if not password:
            raise HTTPException(status_code=400, detail="Password is required")
        if len(password) < 8:
            raise HTTPException(status_code=400, detail="Password must be at least 8 characters long")
        return password.strip()
