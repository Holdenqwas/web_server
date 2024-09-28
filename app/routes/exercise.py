from pydantic.v1.schema import schema
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import APIRouter, HTTPException, Path, Depends
from typing import Union

from app.utils.database import get_db
from app.utils.auth import require_user
from app.crud import training as crud
from app.schemas import training as training_schema

router = APIRouter()


@router.post("/write_exercise", response_model=training_schema.ExerciseDTO)
async def write_exercise(
    data: training_schema.TrainingDTO,
    # user: str = Depends(require_user),
    db: AsyncSession = Depends(get_db),
):
    await crud.write_exercise(data, db)
