from pydantic.v1.schema import schema
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import APIRouter, HTTPException, Path, Depends
from typing import Union

from app.utils.database import get_db
from app.utils.auth import require_user
from app.crud import exercise as crud
from app.schemas import exercise as exercise_schema

router = APIRouter()


@router.post("/write_exercise")
async def write_exercise(
    data: exercise_schema.ExerciseDTO,
    # user: str = Depends(require_user),
    db: AsyncSession = Depends(get_db),
):
    await crud.write_exercise(data, db)


@router.get("/{name_train}/{name_exercise}")
async def get_last_exercise(
    name_train: str,
    name_exercise: str,
    # user: str = Depends(require_user),
    db: AsyncSession = Depends(get_db),
):
    return await crud.get_last_exercise(name_train, name_exercise, db)
