from fastapi import APIRouter, HTTPException, status, Path, Depends
from .sushiRouter import user_dependency
from repositories.adminRepository import AdminRepository

router = APIRouter(tags=["admin"], prefix="/admin")

@router.get("/sushi_all", status_code=status.HTTP_200_OK)
async def read_all_self_admin(user: user_dependency, admin_repository: AdminRepository = Depends()):
    if user is None or user.get("role") != "ADMIN":
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="El usuario no es administrador",
        )
    return admin_repository.get_all()

@router.delete("/sushi/{sushi_id}", status_code=status.HTTP_204_NO_CONTENT, response_model=None)
async def delete_sushi_self_admin(
    user: user_dependency, admin_repository: AdminRepository = Depends(), sushi_id: int = Path(gt=0)
):
    if user is None or user.get("role") != "ADMIN":
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="El usuario no es administrador",
        )
    if admin_repository.delete(sushi_id) is False:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="El usuario no es administrador",
        )
    
