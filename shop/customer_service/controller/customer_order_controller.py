from fastapi import APIRouter, HTTPException
from starlette import status

from model.customer_order import CustomerOrder
from model.customer_order_request import CustomerOrderRequest
from model.customer_order_response import CustomerOrderResponse
from service import customer_order_service

router = APIRouter(
    prefix="/customer_order",
    tags=["customer_order"]
)


@router.get(path="/{customer_order_id}", response_model=CustomerOrder, status_code=status.HTTP_200_OK)
async def get_by_id(customer_order_id: int) -> CustomerOrder:
    try:
        return await customer_order_service.get_by_id(customer_order_id)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post(path="/", response_model=CustomerOrderResponse, status_code=status.HTTP_201_CREATED)
async def create(customer_order_request: CustomerOrderRequest) -> CustomerOrderResponse:
    try:
        return await customer_order_service.create(customer_order_request)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.put(path="/{customer_order_id}", response_model=CustomerOrderResponse, status_code=status.HTTP_200_OK)
async def update(customer_order_id : int, customer_order_request: CustomerOrderRequest) -> CustomerOrderResponse:
    try:
        return await customer_order_service.update(customer_order_id, customer_order_request)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.delete(path="/{customer_order_id}", status_code=status.HTTP_200_OK)
async def delete(customer_order_id: int):
    try:
        return await customer_order_service.delete(customer_order_id)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
