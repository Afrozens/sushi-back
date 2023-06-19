from pydantic import BaseModel, Field


class UserVerification(BaseModel):
    password: str
    new_password: str = Field(min_length=6)

    class Config:
        schema_extra = {
            "example": {"password": "jesus123", "new_password": "hola123321"}
        }
