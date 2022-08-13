from typing import List
from src.schemas.pet_schema import Pet

from pydantic import BaseModel

class UserBase(BaseModel):
    email: str

class User(UserBase):
    id: int
    pets: List[Pet] = []

    class Config:
        orm_mode = True