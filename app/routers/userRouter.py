from fastapi import APIRouter, HTTPException, status, Depends
from .sushiRouter import user_dependency
from .authRouter import bcrypt_context
from repositories.userRepository import UserRepository
from schemas.userSchemas import UserVerification
from models.authModel import Users

router = APIRouter(tags=["user"], prefix="/user")

@router.get("/", status_code=status.HTTP_200_OK)
async def read_user(user: user_dependency, user_repository: UserRepository = Depends()):
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="El usuario no es valido"
        )
    return user_repository.get_profile(user)

@router.put("/password", status_code=status.HTTP_204_NO_CONTENT)
async def change_password(
    user: user_dependency,
    user_verification: UserVerification,
    user_repository: UserRepository = Depends(),
):
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="El usuario no es valido"
        )
    user_model: Users = user_repository.get_profile(user)
    if not bcrypt_context.verify(
        user_verification.password, user_model.hashed_password
    ):
        raise HTTPException(status_code=401, detail="Error al cambiar la contraseña")
    if user_model is not None:
        user_model.hashed_password = bcrypt_context.hash(user_verification.new_password)
        return user_repository.update_password(user_model)