from typing import Optional, List

from model.customer_order import CustomerOrder
from repository.database import database

TABLE = "customer_order"


async def get_by_id(customer_order_id: int) -> Optional[CustomerOrder]:
    query = f"SELECT * FROM {TABLE} WHERE id=:order_id"
    value = {"order_id": customer_order_id}
    result = await database.fetch_one(query, value)
    if result:
        return CustomerOrder(**result)
    else:
        raise Exception(f"Order with order id: {customer_order_id} does not exist")


async def create(customer_order: CustomerOrder):
    query = f"""
            INSERT INTO {TABLE}
            (customer_id, item_name, price)
            VALUES (:customer_id, :item_name, :price)
            """
    values = {"customer_id": customer_order.customer_id, "item_name": customer_order.item_name,
              "price": customer_order.price}

    await database.execute(query, values)


async def update(customer_order_id: int, customer_order: CustomerOrder):
    query = f"""
        UPDATE {TABLE}
        SET item_name=:item_name,
            price=:price
            WHERE id=:customer_order_id
        """
    values = {"customer_order_id": customer_order_id,
              "item_name": customer_order.item_name,
              "price": customer_order.price}
    await database.execute(query, values)


async def get_all() -> List[CustomerOrder]:
    query = f"SELECT * FROM {TABLE}"
    results = await database.fetch_all(query)
    return [CustomerOrder(**result) for result in results]


async def get_all_by_customer_id(customer_order_id: int) -> List[CustomerOrder]:
    query = f"SELECT * FROM {TABLE} WHERE customer_id=:customer_order_id"
    value = {"customer_order_id": customer_order_id}
    results = await database.fetch_all(query, value)
    customer_orders = [CustomerOrder(**result) for result in results]
    print(customer_orders)
    return customer_orders


async def delete(customer_order_id):
    order = await get_by_id(customer_order_id)
    if order.id is not None:
        query = f"DELETE FROM {TABLE} WHERE id=:customer_order_id"
        value = {"customer_order_id": customer_order_id}
        await database.execute(query, value)
    else:
        raise Exception(f"Order with id {customer_order_id} not exists")
