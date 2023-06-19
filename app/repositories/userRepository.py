from fastapi import Depends
from sqlalchemy.orm import Session
from typing import List

from routers.sushiRouter import user_dependency
from configs.database import get_db
from models.authModel import Users 

class UserRepository:
    db: Session

    def __init__(self, db: Session = Depends(get_db)) -> None:
        self.db = db

    def get_profile(self, user: user_dependency) -> List[Users] | Users:
        return self.db.query(Users).filter(Users.id == user.get("id")).first()

    def update_password(self, user: Users):
        self.db.add(user)
        self.db.commit()
