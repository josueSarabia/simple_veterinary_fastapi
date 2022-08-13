from typing import List
from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session
from src.database.querys import users_query
from src.schemas import user_schema
from src.database.utils import utils

router = APIRouter()


@router.post("/users/", response_model=user_schema.User)
def create_user(user: user_schema.UserBase, db: Session = Depends(utils.get_db)):
    db_user = users_query.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return users_query.create_user(db=db, user=user)


@router.get("/users/", response_model=List[user_schema.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(utils.get_db)):
    users = users_query.get_users(db, skip=skip, limit=limit)
    return users


@router.get("/users/{user_id}", response_model=user_schema.User)
def read_user(user_id: int, db: Session = Depends(utils.get_db)):
    db_user = users_query.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user
