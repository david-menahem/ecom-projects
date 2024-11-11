from pydantic.v1 import BaseSettings


class Config(BaseSettings):
    LAST_FM_BASE_URL = "http://ws.audioscrobbler.com/2.0"
    LAST_FM_API_KEY = "34e0973447d9a9cfb87866adc591e746"