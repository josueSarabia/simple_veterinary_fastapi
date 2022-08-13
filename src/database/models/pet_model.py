from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from src.database.database import Base



class Pet(Base):
    __tablename__ = "pets"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    age = Column(Integer, index=True)
    race = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="pets")