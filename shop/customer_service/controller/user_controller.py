from fastapi import APIRouter
from starlette import status

router = APIRouter(
    prefix="/user",
    tags=["user"]
)


