from fastapi import Depends
from sqlalchemy.orm import Session

from configs.database import get_db
from models.sushiModel import Sushi 

class AdminRepository:
    db: Session

    def __init__(self, db: Session = Depends(get_db)) -> None:
        self.db = db

    def get_all(self) -> list[Sushi]:
        all_sushi = self.db.query(Sushi).all()
        if all_sushi is not None:
            return all_sushi

    def delete(self, id: int) -> None:
        model = (
            self.db.query(Sushi)
            .filter(Sushi.id == id)
            .first()
        )
        if model is None:
            False
        self.db.delete(model)
        self.db.commit()
        self.db.flush()
