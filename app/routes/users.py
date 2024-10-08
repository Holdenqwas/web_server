from pydantic.v1.schema import schema
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import APIRouter, HTTPException, Path, Depends
from typing import Union

from app.utils.database import get_db
from app.utils.auth import require_user
from app.crud import users as crud
from app.schemas import users as users_schema

router = APIRouter()


@router.post("/create", response_model=users_schema.User)
async def create_user(
    data: users_schema.CreateUser,
    user: str = Depends(require_user),
    db: AsyncSession = Depends(get_db),
):
    result = await crud.create_user(data, db)

    if result is None:
        raise HTTPException(status_code=404, detail="Cant create user")

    return result


@router.patch("/update_date_license", response_model=users_schema.User)
async def update_date_license(
    data: users_schema.UpdateDateLicense,
    user: str = Depends(require_user),
    db: AsyncSession = Depends(get_db),
):
    result = await crud.update_date_license(data, db)

    return result


# trainnings
@router.post("/create_trainings", response_model=users_schema.User)
async def create_trainings(
    data: users_schema.NameTrainings,
    user: str = Depends(require_user),
    db: AsyncSession = Depends(get_db),
):
    result = await crud.update_name_trainings(data, db)

    return result


@router.patch("/update_name_trainings", response_model=users_schema.User)
async def update_name_trainings(
    data: users_schema.NameTrainings,
    user: str = Depends(require_user),
    db: AsyncSession = Depends(get_db),
):
    result = await crud.update_name_trainings(data, db)

    return result


@router.delete(
    "/delete_trainings/{user_name}", response_model=users_schema.User
)
async def delete_trainings(
    user_name: str,
    user: str = Depends(require_user),
    db: AsyncSession = Depends(get_db),
):
    result = await crud.delete_trainings(user_name, db)

    return result


# exercises
@router.patch("/update_name_exercises", response_model=users_schema.User)
async def update_name_exercises(
    data: users_schema.NameExercises,
    user: str = Depends(require_user),
    db: AsyncSession = Depends(get_db),
):
    result = await crud.update_name_exercises(data, db)

    return result


@router.post("/create_exercises", response_model=users_schema.User)
async def create_exercises(
    data: users_schema.NameExercises,
    user: str = Depends(require_user),
    db: AsyncSession = Depends(get_db),
):
    result = await crud.update_name_exercises(data, db)

    return result
