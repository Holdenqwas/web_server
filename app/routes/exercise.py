from pydantic.v1.schema import schema
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import APIRouter, HTTPException, Path, Depends
from typing import Union

from app.utils.database import get_db
from app.utils.auth import require_user
from app.crud import training as crud
from app.schemas import training as training_schema

router = APIRouter()


@router.get('/last', response_model=training_schema.TrainingDTO)
async def get_training(user: str = Depends(require_user), db: AsyncSession = Depends(get_db)):
    result = await crud.get_training(db)

    if result is None:
        raise HTTPException(status_code=404,
                            detail='Cant found training')

    return result

@router.get('/{name_training}/{name_exercise}', response_model=float)
async def get_training(name_training: str, name_exercise: str, user: str = Depends(require_user), db: AsyncSession = Depends(get_db)):
    result = await crud.get_last_exercise(name_training, name_exercise, db)

    if result is None:
        return -1

    return result

@router.post('/create', response_model=training_schema.TrainingDTO)
async def create_training(data: training_schema.TrainingDTO, user: str = Depends(require_user), db: AsyncSession = Depends(get_db)):
    result = await crud.create_training(data, db)

    if result is None:
        raise HTTPException(status_code=404,
                            detail='Cant create training')

    return result

@router.patch('/update', response_model=training_schema.TrainingDTO)
async def update_training(data: training_schema.TrainingDTO, user: str = Depends(require_user), db: AsyncSession = Depends(get_db)):
    result = await crud.update_training(data, db)

    return result

@router.post('/write_exercise')
async def write_exercise(data: training_schema.ExerciseDTO, user: str = Depends(require_user), db: AsyncSession = Depends(get_db)):
    result = await crud.write_exercise(data, db)

