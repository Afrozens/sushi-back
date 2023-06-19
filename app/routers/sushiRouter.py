from fastapi import APIRouter, HTTPException, status, Path, Depends
from typing import Annotated

from .authRouter import get_current_user
from schemas.sushiSchemas import SushiSchema
from models.sushiModel import Sushi
from repositories.sushiRepository import SushiRepository

router = APIRouter(tags=["sushi"], prefix="/sushi")

user_dependency = Annotated[dict, Depends(get_current_user)]

@router.get("/{sushi_id}", status_code=status.HTTP_200_OK)
async def read_sushi(
    user: user_dependency, sushi_id: int = Path(gt=0), sushi_repository: SushiRepository = Depends()
):
    if user is None:
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, detail="Autenticacion a fallado")

    sushi_model = sushi_repository.get(sushi_id, user)
    if sushi_model is not None:
        return sushi_model
    raise HTTPException(status.HTTP_404_NOT_FOUND, detail="Este sushi no existe")


@router.post("/create",status_code=status.HTTP_201_CREATED)
async def create_sushi(
    sushi_request: SushiSchema, user: user_dependency, sushi_repository: SushiRepository = Depends()
):
    if user is None:
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, detail="Autenticacion a fallado")
    sushi_model = Sushi(**sushi_request.dict(), owner_id=user.get("id"))
    if sushi_model is not None:
        sushi_repository.create(sushi_model)
    raise HTTPException(status.HTTP_409_CONFLICT, detail="Tus datos son incorrectos")


@router.put("update/{sushi_id}", status_code=status.HTTP_204_NO_CONTENT)
async def update_sushi(
    user: user_dependency,
    sushi_request: SushiSchema,
    sushi_id: int = Path(gt=0),
    sushi_repository: SushiRepository = Depends(),
):
    if user is None:
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, detail="Autenticacion a fallado")
    sushi_model = Sushi(**sushi_request.dict())

    sushi_repository.update(sushi_id, sushi_model, user)


@router.delete("delete/{sushi_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_sushi(
    user: user_dependency, sushi_id: int = Path(gt=0), sushi_repository: SushiRepository = Depends()
):
    if user is None:
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, detail="Autenticacion a fallado")
    sushi_repository.delete(sushi_id, user)
