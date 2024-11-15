from typing import Optional

from pydantic import BaseModel


class User(BaseModel):
    id: Optional[int] = None
    username: str
    first_name: str
    last_name: str
    hashed_password: str
    is_active: bool = True

