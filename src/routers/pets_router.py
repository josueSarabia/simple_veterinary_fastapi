from typing import List
from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session
from src.schemas import pet_schema
from src.database.querys import pets_query
from src.database.utils import utils

router = APIRouter()


@router.post("/users/{user_id}/pets/", response_model=pet_schema.Pet)
def create_pet_for_user(
    user_id: int, pet: pet_schema.PetCreate, db: Session = Depends(utils.get_db)
):
    return pets_query.create_user_pet(db=db, pet=pet, user_id=user_id)

@router.get("/pets/", response_model=List[pet_schema.Pet])
def read_pets(skip: int = 0, limit: int = 100, db: Session = Depends(utils.get_db)):
    pets = pets_query.get_pets(db, skip=skip, limit=limit)
    return pets
