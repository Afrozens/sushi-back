from fastapi import APIRouter, HTTPException, status, Path, Depends
from schemas.sushiSchemas import SushiSchema
from models.sushiModel import Sushi
from repositories.sushiRepository import SushiRepository

router = APIRouter(tags=["sushi"], prefix="/sushi")

# @router.get("/all")
# async def read_all_sushis(db: db_dependency):
#     return db.query(Sushi).all()


@router.get("/{sushi_id}", status_code=status.HTTP_200_OK)
async def read_sushi(
    sushi_id: int = Path(gt=0), sushi_repository: SushiRepository = Depends()
):
    sushi_model = sushi_repository.get(Sushi, sushi_id)
    if sushi_model is not None:
        return sushi_model
    raise HTTPException(status.HTTP_404_NOT_FOUND, detail="Este sushi no existe")


@router.post("/create", status_code=status.HTTP_201_CREATED)
async def create_sushi(
    sushi_request: SushiSchema, sushi_repository: SushiRepository = Depends()
):
    sushi_model = Sushi(**sushi_request.dict())
    if sushi_model is not None:
        sushi_repository.create(sushi_model)
    raise HTTPException(status.HTTP_409_CONFLICT, detail="Tus datos son incorrectos")


@router.put("update/{sushi_id}", status_code=status.HTTP_204_NO_CONTENT)
async def update_sushi(
    sushi_request: SushiSchema,
    sushi_id: int = Path(gt=0),
    sushi_repository: SushiRepository = Depends(),
):
    sushi_model = Sushi(**sushi_request.dict())

    sushi_repository.update(sushi_id, sushi_model)


@router.delete("delete/{sushi_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_sushi(
    sushi_id: int = Path(gt=0), sushi_repository: SushiRepository = Depends()
):
    sushi_repository.delete(Sushi(id=sushi_id))
