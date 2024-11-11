from fastapi import APIRouter, HTTPException
from redis_client.redis_client import redis_client

router = APIRouter(
    prefix="/redis",
    tags=["redis"]
)


@router.post(path="/test")
async def redis_test(redis_key: str, redis_value: str):
    try:
        redis_client.setex(redis_key, 100, redis_value)
        return f'Redis key: {redis_key} Redis value: {redis_value}'
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
