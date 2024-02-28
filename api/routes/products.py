from fastapi import APIRouter, Request, Body

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
async def create_product(request: Request, body: dict = Body(...)):
    return await productController.create_product(request, body)

@router.put("/{product_id}")
async def update_product(request: Request, product_id: str, body: dict = Body(...)):
    return await productController.update_product(request, product_id, body)

@router.delete("/{product_id}")
async def delete_product(request: Request, product_id: str):
    return await productController.delete_product(request, product_id)
