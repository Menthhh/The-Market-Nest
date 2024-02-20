from fastapi import responses, HTTPException

async def getUsers(request):
    try:
        message = {"text": "User"}
        return message
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))