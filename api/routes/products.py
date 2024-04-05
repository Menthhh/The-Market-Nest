from fastapi import APIRouter, Request, Body
from fastapi import UploadFile, File

from controller.products import ProductController

router = APIRouter()

productController = ProductController()


@router.get("/")
async def get_products(request: Request):
    return await productController.get_products(request)

@router.get("/find/{product_id}")
async def get_product(request: Request, product_id: str):
    return await productController.get_product(request, product_id)

@router.post("/")
async def create_product(request: Request, title: str, category: str, description: str, price: int, amount: int, address :str , user_id : str, image: UploadFile = UploadFile(...)):
    return await productController.create_product(request, title, category, description, price, amount, address, user_id, image)


@router.put("/{product_id}")
async def update_product(request: Request, product_id: str, body: dict = Body(...)):
    return await productController.update_product(request, product_id, body)

@router.delete("/{product_id}/{user_id}")
async def delete_product(request: Request, product_id: str, user_id: str):
    return await productController.delete_product(request, product_id, user_id)

@router.get("/images/{product_id}")
async def get_product_images(request: Request, product_id: str):
    return await productController.get_product_photo(request, product_id)
