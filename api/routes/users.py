from fastapi import APIRouter, Request
from controller import users

router = APIRouter()

@router.get("/")
async def getUsers(request: Request):
    return await users.getUsers(request)