from fastapi import HTTPException
from model.product import Product
from db.ZODBs import ZODBs


product_db = ZODBs("api/db/Storage/products.fs")
product_db.connect()

async def createProduct(request, body):
    try:
        newProduct = Product(body["title"], body["category"], body["description"], body["price"], body["amount"])
        saveProduct = product_db.create(newProduct)
        return saveProduct
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


async def getProducts(request):
    try:
        """
        products means all the products, 
        loop through throgh root database and append to products list
        """
        products = []
        for item in product_db.findAll():
            products.append(item)
        return products
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    
async def getProduct(request, product_id):
    try:
        """
        find the product by product_id
        """
        getProduct = product_db.findOne(product_id)
        return getProduct
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
async def updateProduct(request, product_id, body):
    try:
        """
        update the product by product_id
        """
        updateProduct = product_db.findOneAndUpdate(product_id, body)
        return updateProduct
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    

    