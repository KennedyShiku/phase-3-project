# lib/client.py
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .database import Base

class Client(Base): 
    __tablename__ = "clients"

    client_id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)

    contents = relationship("Content", back_populates="client")

    def __repr__(self):
        return f"Client(client_id={self.client_id}, name={self.name})"
