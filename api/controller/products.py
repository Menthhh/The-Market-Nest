from fastapi import HTTPException
from model.product import Product
from db.Warehouse import Warehouse
import sys

class ProductController:
    def __init__(self):
        # Specify the 'products' storage when creating the Warehouse instance
        self.__products_db = Warehouse(('127.0.0.1', 8100))
        self.__products_db.connect()
    
    async def create_product(self, request, body):
        try:
            """
            create new Product object
            """
            new_product = Product(body["title"], body["category"], body["description"], body["price"], body["amount"])
            saved_product = self.__products_db.create(new_product)
            return saved_product
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    
    async def get_products(self, request):
        try:
            """
            Get all products from the database
            """
            products = self.__products_db.findAll()
            # Filter out non-Product instances
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
                return product
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
    
    async def delete_product(self, request, product_id):
        try:
            """
            Delete a product by its product_id
            """
            deleted_product = self.__products_db.findOneAndDelete(product_id)
            if deleted_product:
                return {"message": "Product deleted successfully"}
            else:
                raise HTTPException(status_code=404, detail="Product not found")
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
