# NEED TO RUN WITH uvicorn src.main:app --reload

from fastapi import FastAPI
from .routers import pets_router, users_router
from .database.database import engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(pets_router.router)
app.include_router(users_router.router)
