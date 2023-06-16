
from typing import Optional
from pydantic import BaseModel

class authRequest(BaseModel):
    id: Optional[str]
    username: str
    first_name: str
    last_name: str
    email: str
    password: str
    role: str
    is_active: Optional[bool]

class token(BaseModel):
    access_token: str
    token_type: str