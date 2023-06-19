from typing import Optional
from pydantic import BaseModel, Field, EmailStr


class authRequest(BaseModel):
    id: Optional[str]
    username: str = Field(min_length=5)
    first_name: str = Field(min_length=5)
    last_name: str = Field(min_length=5)
    email: EmailStr
    password: str = Field(
        min_length=5, max_length=48, regex=r"^(?=.*[A-Z])(?=.*\d).+$"
    )  # password with a word and a number.
    role: str = Field(min_length=4, default="USER")
    is_active: Optional[bool]

    class Config:
        schema_extra = {
            "example": {
                "id": "f963e1b2-271c-45f8-a9a6-cfd0d921ed28'",
                "username": "afroZen",
                "first_name": "jesús",
                "last_name": "chacón",
                "email": "jesuszen2.6@gmail.com",
                "password": "Jesus123",
                "role": "USER",
                "is_active": True
            }
        }

class token(BaseModel):
    access_token: str
    token_type: str