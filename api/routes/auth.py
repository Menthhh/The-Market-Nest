from fastapi import APIRouter, Request, Body

from controller.auth import AuthController

router = APIRouter()
authController = AuthController()


@router.post("/")
async def login(request: Request, body: dict = Body(...)):
    return await authController.login(request, body)


