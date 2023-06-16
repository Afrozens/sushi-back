from sqlalchemy import Column, String, Boolean
from configs.database import Base

class Users(Base):
    __tablename__ = "users"

    id = Column(String, primary_key=True, index=True) 
    email = Column(String, unique=True)
    username = Column(String, unique=True)
    first_name = Column(String)
    last_name = Column(String)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
    role = Column(String)
