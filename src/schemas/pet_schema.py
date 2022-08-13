from typing import Union

from pydantic import BaseModel


class PetBase(BaseModel):
    name: str
    age: int
    race: str

class PetCreate(PetBase):
    pass

class Pet(PetBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True