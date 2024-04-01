from fastapi import HTTPException
from db.Warehouse import Warehouse
from model.user import User
import sys

class AuthController:
    def __init__(self):
        self.__users_db = Warehouse(('127.0.0.1', 8100))
        self.__users_db.connect()
    
    async def login(self, request, body):
        try:
            """
            login the user by username and password
            """
            users = [user for user in self.__users_db.findAll() if isinstance(user, User)]

            username = body["username"]
            password = body["password"]

            for user in users:
                if username == user.username and password == user.password:
                    return {"token": user._id}

                
                
            return {"error": "Invalid username or password"}, 401
    
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    
