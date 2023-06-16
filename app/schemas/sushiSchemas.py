from typing import Optional, Dict
from pydantic import BaseModel, Field

class SushiRequest(BaseModel):
    name: str = Field(min_length=3)
    description: str = Field(min_length=24, max_length=150)
    price: float = Field(gt=0, lt=24.99)
    image: str = Field(min_length=5)
    isThere: bool 
    historyReview: Optional[Dict]

class SushiSchema(SushiRequest):
    id: int = Field(gt=0)