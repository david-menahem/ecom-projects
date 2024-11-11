from typing import List

from exceptions.customer_not_found_exception import CustomerNotFoundException
from model.customer import Customer
from model.customer_status import CustomerStatus
from repository.database import database

TABLE_NAME = "customer"


async def get_by_id(customer_id: int) -> Customer:
    query = f"SELECT * FROM {TABLE_NAME} WHERE id=:customer_id"
    result = await database.fetch_one(query, values={"customer_id": customer_id})
    if result:
        return Customer(**result)
    else:
        raise Exception(f"Customer with id: {customer_id} does not exist")


async def get_all() -> List[Customer]:
    query = f" SELECT * FROM {TABLE_NAME}"
    results = await database.fetch_all(query)
    return [Customer(**result) for result in results]


async def get_by_status(customer_status: CustomerStatus) -> List[Customer]:
    query = f"SELECT * FROM {TABLE_NAME} WHERE status=:customer_status"
    results = await database.fetch_all(query, values={"customer_status": customer_status.name})
    return [Customer(**result) for result in results]


async def create(customer: Customer) -> int:
    query = f"""
            INSERT INTO {TABLE_NAME} (first_name, last_name, email ,status)
            VALUES (:first_name, :last_name, :email, :status)
    """
    values = {"first_name": customer.first_name, "last_name": customer.last_name,
              "email": customer.email, "status": customer.status.name}
    async with database.transaction():
        await database.execute(query, values)
        last_record_id = await database.fetch_one("SELECT LAST_INSERT_ID()")
    return last_record_id[0]


async def update(customer_id: int, customer: Customer):
    query = f"""UPDATE {TABLE_NAME}
     SET first_name=:first_name,
     last_name=:last_name,
     email=:email,
     status=:status
     WHERE id=:customer_id
    """
    values = {"customer_id": customer_id, "first_name": customer.first_name, "last_name": customer.last_name,
              "email": customer.email, "status": customer.status.name}
    await database.execute(query, values)


async def delete(customer_id: int):
    query = (f"UPDATE {TABLE_NAME} SET status=:status "
             f"WHERE id=:customer_id")
    values = {"customer_id": customer_id, "status": CustomerStatus.IN_ACTIVE.name}
    await database.execute(query, values=values)

