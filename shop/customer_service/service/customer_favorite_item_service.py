from typing import Optional, List

from api.internalApi.seller_service import seller_service
from api.internalApi.seller_service.model.Item_response import ItemResponse
from model.customer_favorite_item import CustomerFavoriteItem
from model.customer_favorite_item_request import CustomerFavoriteItemRequest
from repository import customer_favorite_items_repository


async def get_by_customer_id(customer_id: int) -> List[ItemResponse]:
    favorite_item_ids = await customer_favorite_items_repository.get_by_customer_id(customer_id)
    favorite_items = await seller_service.get_favorite_items_by_ids(favorite_item_ids)
    print(favorite_items)
    return favorite_items


async def create(customer_favorite_item_request: CustomerFavoriteItemRequest):
    item = await seller_service.get_lowest_price_item_by_name(customer_favorite_item_request.item_name)
    print(item)
    if item is not None:
        customer_favorite_item = CustomerFavoriteItem(customer_id=customer_favorite_item_request.customer_id,
                                                      item_id=item.id)
        await customer_favorite_items_repository.create(customer_favorite_item)
    else:
        raise Exception('Unable to create favorite item')


async def update(customer_favorite_item: CustomerFavoriteItem):
    await customer_favorite_items_repository.update(customer_favorite_item)


async def delete(favorite_item_id: int):
    await customer_favorite_items_repository.delete(favorite_item_id)
