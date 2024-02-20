import uvicorn
from fastapi import FastAPI
from routes.products import router as product_router
from routes.users import router as user_router

app = FastAPI()

app.include_router(product_router, prefix="/api/products", tags=["products"])
app.include_router(user_router, prefix="/api/users", tags=["users"])

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=9000)
