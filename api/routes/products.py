from fastapi import APIRouter,Request, Body
from controller import products

router = APIRouter()


@router.get("/")
async def getProducts(request: Request):
    return await products.getProducts(request)

@router.post("/")
async def createProduct(request: Request, body: dict = Body(...) ):
    return await products.createProduct(request, body)