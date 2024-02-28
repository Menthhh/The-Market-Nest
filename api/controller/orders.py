from fastapi import HTTPException
from model.product import Product
from db.Warehouse import Warehouse

class OrderController:
    def __init__(self):
        self.__products_db = Warehouse("c:/Users/Tonkla/Desktop/The-Market-Nest/api/db/Storage/orders/products.fs")
        self.__products_db.connect()
    
    async def create_product(self, request, body):
        try:
            """
            create new Object lifeline
            """
            new_product = Product(body["title"], body["category"], body["description"], body["price"], body["amount"])
            saved_product = self.__products_db.create(new_product)
            return saved_product
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    
    async def get_products(self, request):
        try:
            """
            products means all the products, 
            loop through throgh root database and append to products list
            """
            products = self.__products_db.findAll()
            return products
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    
    async def get_product(self, request, product_id):
        try:
            """
            find the product by product_id
            """
            product = self.__products_db.findOne(product_id)
            return product
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    async def update_product(self, request, product_id, body):
        try:
            """
            update the product by product_id
            """
            product = self.__products_db.findOne(product_id)
            updated_product = Product(
                body.get("title", product.title),
                body.get("category", product.category),
                body.get("description", product.description),
                body.get("price", product.price),
                body.get("amount", product.amount)
            )
            saved_product = self.__products_db.findOneAndUpdate(product_id, updated_product)
            return saved_product
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
    
    async def delete_product(self, request, product_id):
        try:
            """
            delete the product by product_id
            """
            deleted_product = self.__products_db.findOneAndDelete(product_id)
            return deleted_product
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))