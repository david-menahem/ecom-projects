from typing import List
from model.customer import Customer
from model.customer_status import CustomerStatus
from repository import customer_repository


async def get_by_id(customer_id: int) -> Customer:
    return await customer_repository.get_by_id(customer_id)


async def get_all() -> List[Customer]:
    return await customer_repository.get_all()


async def create(customer: Customer) -> Customer:
    if customer.status == CustomerStatus.VIP:
        vip_customers = await customer_repository.get_by_status(CustomerStatus.VIP)
        if len(vip_customers) >= 10:
            raise Exception("Can't create status VIP - Out of limit")
        else:
            customer_id = await customer_repository.create(customer)
            return await customer_repository.get_by_id(customer_id)
    else:
        customer_id = await customer_repository.create(customer)
        return await customer_repository.get_by_id(customer_id)


async def update(customer_id: int, customer: Customer) -> Customer:
    existing_customer = await customer_repository.get_by_id(customer_id)
    if existing_customer:
        if customer.status == CustomerStatus.VIP and existing_customer is not CustomerStatus.VIP:
            vip_customers = await customer_repository.get_by_status(CustomerStatus.VIP)
            if len(vip_customers) >= 10:
                raise Exception(f"Cannot update customer status to VIP - Limit has been reached")
            else:
                await customer_repository.update(customer_id, customer)
                return await customer_repository.get_by_id(existing_customer.id)
        else:
            await customer_repository.update(customer_id, customer)
            return await customer_repository.get_by_id(existing_customer.id)


async def delete(customer_id: int):
    await get_by_id(customer_id)
    await customer_repository.delete(customer_id)
