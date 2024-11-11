from fastapi import APIRouter, HTTPException
from starlette import status

from model.customer import Customer
from service import customer_service

router = APIRouter(
    prefix="/customer",
    tags=["customer"]
)


@router.get(path="/{customer_id}", response_model=Customer, status_code=status.HTTP_200_OK)
async def get_by_id(customer_id: int) -> Customer:
    try:
        return await customer_service.get_by_id(customer_id)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post(path="/", response_model=Customer, status_code=status.HTTP_201_CREATED)
async def create(customer: Customer):
    try:
        return await customer_service.create(customer)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.put(path="/{customer_id}", response_model=Customer, status_code=status.HTTP_200_OK)
async def update(customer_id: int, customer: Customer):
    try:
        return await customer_service.update(customer_id, customer)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.delete(path="/{customer_id}")
async def delete(customer_id: int):
    try:
        await customer_service.delete(customer_id)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
