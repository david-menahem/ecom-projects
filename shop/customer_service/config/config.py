from pydantic.v1 import BaseSettings


class Config(BaseSettings):
    MYSQL_DATABASE: str = "customer"
    MYSQL_USER: str = "user"
    MYSQL_PASSWORD: str = "123456"
    MYSQL_HOST: str = "localhost"
    MYSQL_PORT: str = "3309"
    DATABASE_URL: str = f'mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DATABASE}'
    SELLER_SERVICE_BASE_URL = "http://localhost:8000"
    REDIS_HOST = "localhost"
    REDIS_PORT = "6379"
    REDIS_TTL = 100
    SECRET_KEY: str = "secret_key_app"
    ALGORITHM: str = "HS256"
    TOKEN_EXPIRY_TIME: float = 20.0






