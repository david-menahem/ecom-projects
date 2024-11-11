from typing import List, Optional

import httpx

from config.config import Config
from api.internalApi.seller_service.model.Item_response import ItemResponse

config = Config()


async def get_favorite_items_by_ids(favorite_item_ids) -> List[ItemResponse]:

    url = f"{config.SELLER_SERVICE_BASE_URL}/item/customer_favorite"
    params = {
        "favorite_item_ids": favorite_item_ids
    }

    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url, params=params)
            print(response)
            response.raise_for_status()
            results = response.json()

            return [ItemResponse(**result) for result in results]
        except Exception as e:
            raise e


async def get_lowest_price_item_by_name(item_name: str) -> Optional[ItemResponse]:
    url = f'{config.SELLER_SERVICE_BASE_URL}/item/lowest_price/{item_name}'
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url)
            response.raise_for_status()
            data = response.json()
            item_response = ItemResponse(
                id=data.get("id"),
                seller_id=data.get("seller_id"),
                item_name=data.get("item_name"),
                price=data.get("price")
            )
            print(item_response)
            return item_response
        except httpx.HTTPStatusError as e:
            print(f"Error getting information for item {item_name} with error {e.response}")
            return None





# async def get_by_id(favorite_item_id) -> CustomerFavoriteItemResponse:
#
# async def get_item_by_id(item_id) -> ItemResponse:
#
# async def get_favorite_items_by_customer_id(customer_id: int) -> List[CustomerFavoriteItemResponse]:
