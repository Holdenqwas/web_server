from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import APIRouter, HTTPException, Depends

from app.crud import users as crud
from app.crud.auth import generate_verify_code
from app.schemas import users as users_schema
from app.utils.auth import require_token_service
from app.utils.database import get_db

router = APIRouter()


@router.post("/create", response_model=users_schema.User)
async def create_user(
    data: users_schema.CreateUser,
    token: str = Depends(require_token_service),
    db: AsyncSession = Depends(get_db),
):
    result = await crud.create_user(data, db)

    if result is None:
        raise HTTPException(status_code=404, detail="Cant create user")

    return result


@router.patch("/update_date_license", response_model=users_schema.User)
async def update_date_license(
    data: users_schema.UpdateDateLicense,
    token: str = Depends(require_token_service),
    db: AsyncSession = Depends(get_db),
):
    result = await crud.update_date_license(data, db)

    return result


# trainnings
@router.post("/create_trainings", response_model=users_schema.User)
async def create_trainings(
    data: users_schema.NameTrainings,
    token: str = Depends(require_token_service),
    db: AsyncSession = Depends(get_db),
):
    result = await crud.update_name_trainings(data, db)

    return result


@router.patch("/update_name_trainings", response_model=users_schema.User)
async def update_name_trainings(
    data: users_schema.NameTrainings,
    token: str = Depends(require_token_service),
    db: AsyncSession = Depends(get_db),
):
    result = await crud.update_name_trainings(data, db)

    return result


@router.delete("/delete_trainings/{user_id}", response_model=users_schema.User)
async def delete_trainings(
    user_id: str,
    token: str = Depends(require_token_service),
    db: AsyncSession = Depends(get_db),
):
    result = await crud.delete_trainings(user_id, db)

    return result


# exercises
@router.patch("/update_name_exercises", response_model=users_schema.User)
async def update_name_exercises(
    data: users_schema.NameExercises,
    token: str = Depends(require_token_service),
    db: AsyncSession = Depends(get_db),
):
    result = await crud.update_name_exercises(data, db)

    return result


@router.post("/create_exercises", response_model=users_schema.User)
async def create_exercises(
    data: users_schema.NameExercises,
    token: str = Depends(require_token_service),
    db: AsyncSession = Depends(get_db),
):
    result = await crud.update_name_exercises(data, db)

    return result


@router.get("/connect_to_alice", response_model=users_schema.VerificateCode)
async def connect_to_alice(
    user_id: int,
    shop_list_name: str,
    token: str = Depends(require_token_service),
    db: AsyncSession = Depends(get_db),
):
    user = await generate_verify_code(user_id, shop_list_name, db)
    return users_schema.VerificateCode(code=user.vefiry_code)
