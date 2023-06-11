from typing import Annotated, Dict, Optional
from uuid import uuid4 as uuid
from pydantic import BaseModel, Field
from fastapi import FastAPI, Depends, HTTPException, status, Path
from sqlalchemy.orm import Session
from models.sushi import Base as SushiBase, Sushi 
#from models.product import Base as ProductBase, Product
from .configs.Database import engine, get_db

app = FastAPI()

SushiBase.metadata.create_all(bind=engine)


db_dependecy = Annotated[Session, Depends(get_db)]

class SushiRequest(BaseModel):
    name: str = Field(min_length=3)
    description: str = Field(min_length=24, max_length=150)
    price: float = Field(gt=0, lt=24.99)
    image: str = Field(min_length=5)
    isThere: bool 
    historyReview: Optional[Dict] = Field()

@app.get("/")
async def read_all_sushis(db: db_dependecy):
    return db.query(Sushi).all()


@app.get("/sushi/{sushi_id}", status_code=status.HTTP_200_OK)
async def read_sushi(db: db_dependecy, sushi_id: str = Path(min_length=8)):
    sushi_model = db.query(Sushi).filter(Sushi.id == sushi_id).first()
    if sushi_model is not None:
        return sushi_model
    raise HTTPException(status.HTTP_404_NOT_FOUND, detail="Este sushi no existe")

@app.post("/sushi/create", status_code=status.HTTP_201_CREATED)
async def create_sushi(db: db_dependecy, sushi_request: SushiRequest):
    sushi_request.id: str == uuid()
    sushi_model = Sushi(**sushi_request.dict())
    
    db.add(sushi_model)
    db.commit()