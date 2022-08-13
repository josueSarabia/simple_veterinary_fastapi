from sqlalchemy.orm import Session

from src.schemas import pet_schema
from src.database.models import pet_model


def get_pets(db: Session, skip: int = 0, limit: int = 100):
    return db.query(pet_model.Pet).offset(skip).limit(limit).all()


def create_user_pet(db: Session, pet: pet_schema.PetCreate, user_id: int):
    db_pet = pet_model.Pet(**pet.dict(), owner_id=user_id)
    db.add(db_pet)
    db.commit()
    db.refresh(db_pet)
    return db_pet