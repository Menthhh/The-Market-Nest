from fastapi import HTTPException
from model.product import Product
from db.Warehouse import Warehouse
from fastapi import FastAPI, UploadFile, HTTPException
from fastapi.responses import FileResponse
from model.user import User
import os
import uuid
import os
from dotenv import load_dotenv
load_dotenv()
UPLOAD_DIRECTORY = os.getenv("UPLOAD_DIRECTORY")
class ProductController:
    def __init__(self):
        self.__products_db = Warehouse(('127.0.0.1', 8100))
        self.__products_db.connect()
    
    async def create_product(self, request, title: str, category: str, description: str, price: int, amount: int, address : str, user_id, image):
        if not os.path.exists(UPLOAD_DIRECTORY):
            os.makedirs(UPLOAD_DIRECTORY)

        try:
            image.filename = uuid.uuid4().hex + "_" + image.filename
            image_path = os.path.join(UPLOAD_DIRECTORY, image.filename)
            with open(image_path, "wb") as file_object:
                file_object.write(await image.read())
            new_product = Product(
                title=title,
                category=category,
                description=description,
                price=price,
                amount=amount,
                address=address
            )
            new_product.photos.append(image_path)
            saved_product = self.__products_db.create(new_product)

            current_user = self.__products_db.findOne(user_id)
            current_user.products.append(saved_product._id)

            if isinstance(current_user, User):
                updated_user = User(
                    current_user.name,
                    current_user.birthDate,
                    current_user.citizenID,
                    current_user.phoneNumber,
                    current_user.email,
                    current_user.username,
                    current_user.password,

                )
                updated_user.products = current_user.products
                updated_user = self.__products_db.findOneAndUpdate(user_id, updated_user)
            
            return {"message": "Product created successfully", "product": saved_product, "user": updated_user}
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    
    async def get_products(self, request):
        try:
            """
            Get all products from the database
            """
            products = self.__products_db.findAll()
            products = [product for product in products if isinstance(product, Product)]
            return products
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

        
    async def get_product(self, request, product_id):
        try:
            """
            Find a product by its product_id
            """
            product = self.__products_db.findOne(product_id)
            if isinstance(product, Product):
                product_return = {
                    "_id": product._id,
                    "title": product.title,
                    "category": product.category,
                    "description": product.description,
                    "price": product.price,
                    "amount": product.amount,
                    "address": product.address,
                    "photos": product.photos
                }
                return (product_return)

            else:
                raise HTTPException(status_code=404, detail="Product not found")
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    async def update_product(self, request, product_id, body):
        try:
            """
            Update a product by its product_id
            """
            product = self.__products_db.findOne(product_id)
            if isinstance(product, Product):
                updated_product = Product(
                    body.get("title", product.title),
                    body.get("category", product.category),
                    body.get("description", product.description),
                    body.get("price", product.price),
                    body.get("amount", product.amount)
                )
                saved_product = self.__products_db.findOneAndUpdate(product_id, updated_product)
                return saved_product
            else:
                raise HTTPException(status_code=404, detail="Product not found")
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
    
    async def delete_product(self, request, product_id, user_id):
        try:
            """
            Delete a product by its product_id
            """
            user = self.__products_db.findOne(user_id)
            user.products.remove(product_id)   
            updated_user = User(
                user.name,
                user.birthDate,
                user.citizenID,
                user.phoneNumber,
                user.email,
                user.username,
                user.password
            )

            self.__products_db.findOneAndDelete(product_id)
       
            updated_user.products = user.products
            updated_user = self.__products_db.findOneAndUpdate(user_id, updated_user)
           
            return {"message": "Product deleted successfully", "user": updated_user}
        
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    async def get_product_photo(self,request, product_id: str):
        try:
            current_product = self.__products_db.findOne(product_id)
            
            if isinstance(current_product, Product):
                for photo in current_product.photos:
                    return FileResponse(photo)
                return {"message": "Product has no photo"}
            else:
                return {"message": "Product not found"}
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
            

            