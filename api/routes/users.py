from fastapi import APIRouter, Request, Body
from controller.users import UserController

router = APIRouter()

userController = UserController()


@router.get("/")
async def get_users(request: Request):
    return await userController.get_users(request)

@router.get("/find/{user_id}")
async def get_user(request: Request, user_id: str):
    return await userController.get_user(request, user_id)

@router.post("/")
async def create_user(request: Request, body: dict = Body(...)):
    return await userController.create_user(request, body)

@router.post("/{user_id}")
async def add_user_photo(request: Request, user_id: str ,body: dict = Body(...)):
    return await userController.add_user_photo(request, user_id, body)

@router.put("/{user_id}")
async def update_user(request: Request, user_id: str, body: dict = Body(...)):
    return await userController.update_user(request, user_id, body)

@router.delete("/{user_id}")
async def delete_user(request: Request, user_id: str):
    return await userController.delete_user(request, user_id)

@router.get("/getUserFromProduct/{product_id}")
async def getUserFromProduct(request: Request, product_id: str):
    return await userController.get_user_by_product_id(request, product_id)