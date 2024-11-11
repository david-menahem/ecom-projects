from typing import List

from model.customer_favorite_item import CustomerFavoriteItem
from repository.database import database
from service import customer_service

table = "customer_favorite_items"


async def get_by_customer_id(customer_id: int) -> []:
    await customer_service.get_by_id(customer_id)
    query = f"SELECT item_id FROM {table} WHERE customer_id=:customer_id"
    value = {"customer_id": customer_id}
    favorite_item_ids = await database.fetch_all(query, value)
    favorite_item_ids_array =[]
    for favorite_item_id in favorite_item_ids:
        favorite_item_ids_array.append(favorite_item_id[0])
    return favorite_item_ids_array


async def create(customer_favorite_item: CustomerFavoriteItem):
    query = f"""
    INSERT INTO {table}
    (customer_id, item_id)
    VALUES
    (:customer_id, :item_id)
    """
    values = {"customer_id": customer_favorite_item.customer_id, "item_id": customer_favorite_item.item_id}
    await database.execute(query, values)


async def update(customer_favorite_item: CustomerFavoriteItem):
    query = f"""
    UPDATE {table} SET
    item_id=:item_id
    WHERE
    id=:id
    """
    values = {"id": customer_favorite_item.id, "item_id": customer_favorite_item.item_id}
    await database.execute(query,values)


async def delete(customer_favorite_item_id: int):
    query = f"DELETE FROM {table} WHERE id=:id"
    value = {"id": customer_favorite_item_id}
    await database.execute(query, value)

