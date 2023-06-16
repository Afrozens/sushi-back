from sqlalchemy import Column, Float, String, Boolean, JSON, Integer, ForeignKey
from configs.database import Base

class Sushi(Base):
    __tablename__ = "sushis"

    id = Column(Integer, primary_key=True, index=True) 
    name = Column(String)
    description = Column(String)
    price = Column(Float)
    image = Column(String)
    isThere = Column(Boolean, default=False)
    historyReview = Column(JSON)
    owner_id = Column(Integer, ForeignKey("users.id"))