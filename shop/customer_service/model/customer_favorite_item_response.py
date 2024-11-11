from pydantic import BaseModel

from api.internalApi.seller_service.model.Item_response import ItemResponse


class CustomerFavoriteItemResponse(BaseModel):
    id: int
    customer_id: int
    item_response: ItemResponse
