from typing import List

from fastapi import APIRouter, HTTPException
from starlette import status

from api.internalApi.seller_service.model.Item_response import ItemResponse
from model.customer_favorite_item import CustomerFavoriteItem
from model.customer_favorite_item_request import CustomerFavoriteItemRequest
from service import customer_favorite_item_service, customer_service

router = APIRouter(
    prefix="/favorite_item",
    tags=["favorite_item"]
)


@router.get(path="/{customer_id}", response_model=List[ItemResponse], status_code=status.HTTP_200_OK)
async def get_by_customer_id(customer_id: int) -> List[ItemResponse]:
    try:
        await customer_service.get_by_id(customer_id)
        return await customer_favorite_item_service.get_by_customer_id(customer_id)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post(path="/", status_code=status.HTTP_201_CREATED)
async def create(customer_favorite_item_request: CustomerFavoriteItemRequest):
    try:
        print("hit")
        await customer_favorite_item_service.create(customer_favorite_item_request)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.put(path="/", status_code=status.HTTP_200_OK)
async def update(customer_favorite_item: CustomerFavoriteItem):
    try:
        await customer_favorite_item_service.update(customer_favorite_item)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.delete(path="/{favorite_item_id}", status_code=status.HTTP_200_OK)
async def delete(favorite_item_id: int):
    await customer_favorite_item_service.delete(favorite_item_id)