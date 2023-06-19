from fastapi import Depends
from sqlalchemy.orm import Session

from configs.database import get_db
from models.sushiModel import Sushi

class SushiRepository:
    db: Session

    def __init__(self, db: Session = Depends(get_db)) -> None:
        self.db = db

    def get(self, id: int, user) -> Sushi:
        return (
            self.db.query(Sushi)
            .filter(Sushi.id == id)
            .filter(Sushi.owner_id == user.get("id"))
            .first()
        )

    def create(self, sushi: Sushi) -> Sushi:
        self.db.add(sushi)
        self.db.commit()
        self.db.refresh(sushi)
        return sushi

    def update(self, id: int, sushi: Sushi, user) -> Sushi:
        sushi.id = id
        sushi_model = self.db.query(sushi.owner_id == user.get("id")).first()
        self.db.merge(sushi_model)
        self.db.commit()
        return sushi_model

    def delete(self, id: int, user) -> None:
        sushi_model = (
            self.db.query(Sushi)
            .filter(Sushi.id == id)
            .filter(Sushi.owner_id == user.get("id"))
            .first()
        )
        if sushi_model is None:
           return False
        self.db.delete(sushi_model)
        self.db.commit()
        self.db.flush()
