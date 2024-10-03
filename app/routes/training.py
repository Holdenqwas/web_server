from pydantic.v1.schema import schema
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import APIRouter, HTTPException, Path, Depends
from typing import Union

from app.utils.database import get_db
from app.utils.auth import require_user
from app.crud import training as crud
from app.schemas import training as training_schema

router = APIRouter()


@router.post("/create", response_model=training_schema.TrainingDTO)
async def create_training_all(
    data: training_schema.CreateTrainingAll,
    # user: str = Depends(require_user),
    db: AsyncSession = Depends(get_db),
):
    result = await crud.create_training_all(data, db)

    if result is None:
        raise HTTPException(status_code=404, detail="Cant create training")

    return result


@router.post("/create_train", response_model=training_schema.TrainingDTO)
async def create_train(
    data: training_schema.CreateTrain,
    # user: str = Depends(require_user),
    db: AsyncSession = Depends(get_db),
):
    result = await crud.create_train(data, db)

    if result is None:
        raise HTTPException(status_code=404, detail="Cant create train")

    return result


@router.post("/name_exercises", response_model=training_schema.NameExercises)
async def get_name_exercises(
    data: training_schema.NameExercise,
    # user: str = Depends(require_user),
    db: AsyncSession = Depends(get_db),
):
    result = await crud.get_name_exercise(data, db)

    if result is None:
        raise HTTPException(status_code=404, detail="Cant get exercise")

    data.name_exercises = result
    return data