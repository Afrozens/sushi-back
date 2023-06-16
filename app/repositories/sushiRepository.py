from fastapi import Depends
from sqlalchemy.orm import Session

from configs.database import get_db
from models.sushiModel import Sushi
from routers.sushiRouter import user_dependency


class SushiRepository:
    db: Session

    def __init__(self, db: Session = Depends(get_db)) -> None:
        self.db = db

    def get(self, sushi: Sushi, id: int, user: user_dependency) -> Sushi:
        return (
            self.db.query(sushi)
            .filter(sushi.id == id)
            .filter(sushi.owner_id == user.get("id"))
            .first()
        )

    def create(self, sushi: Sushi) -> Sushi:
        self.db.add(sushi)
        self.db.commit()
        self.db.refresh(sushi)
        return sushi

    def update(self, id: int, sushi: Sushi, user: user_dependency) -> Sushi:
        sushi.id = id
        sushi_model = self.db.query(sushi.owner_id == user.get("id")).first()
        self.db.merge(sushi_model)
        self.db.commit()
        return sushi_model

    def delete(self, sushi: Sushi, id: int, user: user_dependency) -> None:
        sushi_model = (
            self.db.query(sushi)
            .filter(sushi.id == id)
            .filter(sushi.owner_id == user.get("id"))
            .first()
        )
        if sushi_model is None:
            False
        self.db.delete(sushi_model)
        self.db.commit()
        self.db.flush()
