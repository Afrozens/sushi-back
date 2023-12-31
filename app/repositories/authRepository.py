from fastapi import Depends
from sqlalchemy.orm import Session

from configs.database import get_db
from models.authModel import Users 

class AuthRepository:
    db: Session

    def __init__(self, db: Session = Depends(get_db)) -> None:
        self.db = db

    def get(self, username: str):
        user = self.db.query(Users).filter(Users.username == username).first()
        if user is None:
            return False
        return user

    def create(self, user: Users) -> Users:
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)

