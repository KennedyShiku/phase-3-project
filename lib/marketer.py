# lib/marketer.py
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .database import Base

class Marketer(Base):
    __tablename__ = "marketers"

    marketer_id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)

