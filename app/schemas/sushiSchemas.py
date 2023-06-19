from typing import Optional, Dict, List
from pydantic import BaseModel, Field


class SushiRequest(BaseModel):
    name: str = Field(min_length=3)
    description: str = Field(
        min_length=24, title="The description of the sushi", max_length=300
    )
    price: float = Field(gt=0, lt=24.99)
    image: str = Field(min_length=5)
    isThere: bool
    historyReview: Optional[List[Dict]]

    class Config:
        schema_extra = {
            "example": {
                "name": "nigiri",
                "description": "Sushi que combina una bola de arroz sazonado con vinagre y una loncha de pescado crudo, resaltando el sabor fresco del ingrediente principal.",
                "price": 2.99,
                "image": "nigiri.png",
                "isThere": True,
                "historyReview": [
                    {"afrozen": "80%"}, 
                    {"pingui23": "60%"},
                ]
            }
        }


class SushiSchema(SushiRequest):
    id: int = Field(gt=0)

    class Config:
        schema_extra = {
            "example": {
                "id": 1,
                "name": "nigiri",
                "description": "Sushi que combina una bola de arroz sazonado con vinagre y una loncha de pescado crudo, resaltando el sabor fresco del ingrediente principal.",
                "price": 2.99,
                "image": "nigiri.png",
                "isThere": True,
                "historyReview": [
                    {"afrozen": "80%"}, 
                    {"pingui23": "60%"},
                ]
            }
        }
