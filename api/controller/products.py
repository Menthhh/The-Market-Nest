from fastapi import HTTPException
from model.product import Product
from db.ZODBs import ZODBs


product = ZODBs("db/Storage/products.fs")
product.connect()

#create
async def createProduct(request, body):
    newProduct = Product(body["title"], body["category"], body["description"], body["price"], body["amount"])
    try:
        saveProduct = product.create(newProduct)
        return saveProduct
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        product.close()


async def getProducts(request):
    try:
        message = {"text": "Hello World"}
        return message
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    