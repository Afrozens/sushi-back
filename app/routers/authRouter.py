from fastapi import APIRouter, HTTPException, status, Depends
from uuid import uuid4
from models.authModel import Users
from typing import Annotated
from schemas.authSchemas import authRequest, token
from repositories.authRepository import AuthRepository
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from jose import jwt, JWTError
from datetime import timedelta, datetime

router = APIRouter(tags=["auth"], prefix="/auth")

SECREY_KEY = "d38bd67fce05a2c74b53950deda7ff98474b7db6bb239d846addbc33609ee8df"
ALGORITHM = "HS256"

bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_bearer = OAuth2PasswordBearer(tokenUrl="auth/token")

def authenticate_user(username: str, password: str, auth_repository: AuthRepository):
    user = auth_repository.get(username)
    if not user:
        return False
    if not bcrypt_context.verify(password, user.hashed_password):
        return False
    return user


def create_access_token(username: str, user_id: str, role: str,  expires_delta: timedelta):
    print(user_id)
    encode = {"sub": username, "id": user_id, "role": role}
    expires = datetime.utcnow() + expires_delta
    encode.update({"exp": expires})
    return jwt.encode(encode, SECREY_KEY, algorithm=ALGORITHM)

async def get_current_user(token: Annotated[str, Depends(oauth2_bearer)]):
    try:
        payload = jwt.decode(token, SECREY_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        role: str = payload.get("role")
        user_id: str = payload.get("id")
        if user_id is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                detail="usuario no podria ser invalido")
        return {"username": username, "id": user_id, "role": role}
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                detail="usuario no podria ser invalido")

@router.post("/create", status_code=status.HTTP_201_CREATED)
async def create_user(
    create_user_request: authRequest, auth_repository: AuthRepository = Depends()
):
    create_user_model = Users(
        id=str(uuid4()),
        email=create_user_request.email,
        username=create_user_request.username,
        first_name=create_user_request.first_name,
        last_name=create_user_request.last_name,
        role=create_user_request.role,
        hashed_password=bcrypt_context.hash(create_user_request.password),
    )
    print("user", create_user_model)
    auth_repository.create(create_user_model)


@router.post("/token", status_code=status.HTTP_202_ACCEPTED, response_model=token)
async def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    auth_repository: AuthRepository = Depends(),
):
    user = authenticate_user(form_data.username, form_data.password, auth_repository)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Could not validate user."
        )
    token = create_access_token(user.username, user.id, user.role, timedelta(minutes=60))
    return {"access_token": token, "token_type": "bearer"}
