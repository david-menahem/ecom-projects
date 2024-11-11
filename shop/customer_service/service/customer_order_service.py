from exceptions.customer_order_not_found_exception import CustomerOrderNotFoundException
from model.customer_order import CustomerOrder
from model.customer_order_request import CustomerOrderRequest
from model.customer_order_response import CustomerOrderResponse
from repository import customer_order_repository
from service import customer_service


async def get_by_id(customer_order_id: int) -> CustomerOrder:
    try:
        customer_order = await customer_order_repository.get_by_id(customer_order_id)
        return customer_order
    except CustomerOrderNotFoundException as e:
        raise e
    except Exception as e:
        raise Exception(f"Unexpected error: {e}")


async def create(customer_order_request: CustomerOrderRequest) -> CustomerOrderResponse:
    customer = customer_order_request.customer
    if customer.id:
        customer = await customer_service.get_by_id(customer.id)
    else:
        customer.id = await customer_service.create(customer)
    customer_order_request.customer_order.customer_id = customer.id

    await customer_order_repository.create(customer_order_request.customer_order)
    customer_orders = await customer_order_repository.get_all_by_customer_id(
        customer_order_request.customer_order.customer_id)

    return CustomerOrderResponse(customer=customer, customer_orders=customer_orders)


async def update(customer_order_id: int, customer_order_request: CustomerOrderRequest) -> CustomerOrderResponse:
    try:
        customer = await customer_service.get_by_id(customer_order_request.customer.id)
        customer_orders = await customer_order_repository.get_all_by_customer_id(customer_order_request.customer.id)
        for i, customer_order in enumerate(customer_orders):
            if customer_order_id == customer_orders[i].id:
                customer_orders[i] = customer_order_request.customer_order
                customer_orders[i].customer_id = customer.id
                customer_orders[i].id = customer_order_id
                await customer_order_repository.update(customer_order_id, customer_order_request.customer_order)
                return CustomerOrderResponse(customer=customer, customer_orders=customer_orders)
        raise CustomerOrderNotFoundException(f"Customer with id {customer.id} "
                                             f"has no order with id {customer_order_id}")
    except CustomerOrderNotFoundException as e:
        raise e
    except Exception as e:
        raise Exception(e)


async def delete(customer_order_id: int):
    try:
        await get_by_id(customer_order_id)
        await customer_order_repository.delete(customer_order_id)
    except Exception as e:
        raise e
