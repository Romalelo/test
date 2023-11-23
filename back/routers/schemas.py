from datetime import datetime
from typing import Optional, List

from pydantic.dataclasses import dataclass
from pydantic import BaseModel


@dataclass
class User:
    id: int
    username: str
    first_name: str
    last_name: str
    age: int
    created_at: datetime


class UpdateUserSchema(BaseModel):
    id: Optional[int] = None
    username: Optional[str] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    age: Optional[int] = None
    created_at: Optional[datetime] = None


@dataclass
class UserList:
    count: int
    users: List[User]
