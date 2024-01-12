# lib/content.py
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class Content(Base):
    __tablename__ = "contents" 

    content_id = Column(Integer, primary_key=True, index=True)
    campaign_name = Column(String, index=True)
    client_id = Column(Integer, ForeignKey("clients.client_id"))

    client = relationship("Client", back_populates="contents")

    def __repr__(self):
        return f"Content(content_id={self.content_id}, campaign_name={self.campaign_name}, client_id={self.client_id})"