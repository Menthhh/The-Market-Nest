from fastapi import APIRouter,Request, Body
from controller import products

router = APIRouter()

@router.post("/")
async def createProduct(request: Request, body: dict = Body(...) ):
    return await products.createProduct(request, body)

@router.get("/")
async def getProducts(request: Request):
    return await products.getProducts(request)

@router.get("/find/{product_id}")
async def getProduct(request: Request, product_id: str):
    return await products.getProduct(request, product_id)

@router.put("/{product_id}")
async def updateProduct(request: Request, product_id: str, body: dict = Body(...)):
    return await products.updateProduct(request, product_id, body)

@router.delete("/{product_id}")
async def deleteProduct(request: Request, product_id: str):
    return await products.deleteProduct(request, product_id)