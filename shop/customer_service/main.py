from fastapi import FastAPI
from controller.user_controller import router as user_router
from controller.customer_controller import router as customer_router
from controller.customer_order_controller import router as customer_order_router
from controller.customer_favorite_item_controller import router as customer_favorite_item_router
from controller.redis_test_controller import router as redis_test
from repository.database import database

app = FastAPI()


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shut_down():
    await database.disconnect()


app.include_router(user_router)
app.include_router(customer_router)
app.include_router(customer_order_router)
app.include_router(customer_favorite_item_router)
app.include_router(redis_test)