from sqlalchemy import Column, Float, String, Boolean, JSON
from database import Base

class Sushi(Base):
    __tablename__ = "sushi"

    id = Column(String, primary_key=True, index=True) 
    name = Column(String)
    description = Column(String)
    price = Column(Float)
    image = Column(String)
    isThere = Column(Boolean, default=False)
    historyReview = Column(JSON)
