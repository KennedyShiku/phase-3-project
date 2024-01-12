from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .database import Base

class Marketer(Base):
    __tablename__ = "marketers"

    marketer_id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True) 

    def __repr__(self):
        return f"Marketer(marketer_id={self.marketer_id}, name={self.name})"