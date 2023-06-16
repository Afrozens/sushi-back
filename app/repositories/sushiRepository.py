from fastapi import Depends
from sqlalchemy.orm import Session

from configs.database import get_db
from models.sushiModel import Sushi

class SushiRepository:
    db: Session

    def __init__(self, db: Session = Depends(get_db)) -> None:
        self.db = db

    def get(self, sushi: Sushi, id: int) -> Sushi:
        return self.db.query(sushi).get(id)

    def create(self, sushi: Sushi) -> Sushi:
        self.db.add(sushi)
        self.db.commit()
        self.db.refresh(sushi)
        return sushi

    def update(self, id: int, sushi: Sushi) -> Sushi:
        sushi.id = id
        self.db.merge(sushi)
        self.db.commit()
        return sushi

    def delete(self, sushi: Sushi) -> None:
        self.db.delete(sushi)
        self.db.commit()
        self.db.flush()