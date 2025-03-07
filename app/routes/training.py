from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession


from app.crud import training as crud
from app.schemas import training as training_schema
from app.utils.auth import require_token_service
from app.utils.database import get_db

router = APIRouter()


@router.get(
    "/name_trainings/{user_id}",
    response_model=training_schema.NameTrainingsDTO,
)
async def create_training(
    user_id: int,
    token: str = Depends(require_token_service),
    db: AsyncSession = Depends(get_db),
):
    result = await crud.get_name_trains(user_id, db)

    if not result:
        raise HTTPException(status_code=404, detail="Cant get trainings")

    return {"name_trains": result}


@router.post("/create", response_model=training_schema.TrainingDTO)
async def create_training_all(
    data: training_schema.CreateTrainingAll,
    token: str = Depends(require_token_service),
    db: AsyncSession = Depends(get_db),
):
    result = await crud.create_training_all(data, db)

    if result is None:
        raise HTTPException(status_code=404, detail="Cant create training")

    return result


@router.post("/create_train", response_model=training_schema.TrainingDTO)
async def create_train(
    data: training_schema.CreateTrain,
    token: str = Depends(require_token_service),
    db: AsyncSession = Depends(get_db),
):
    result = await crud.create_train(data, db)

    if result is None:
        raise HTTPException(status_code=404, detail="Cant create train")

    return result


@router.post("/name_exercises", response_model=training_schema.NameExercises)
async def get_name_exercises(
    data: training_schema.NameExercises,
    token: str = Depends(require_token_service),
    db: AsyncSession = Depends(get_db),
):
    result = await crud.get_name_exercise(data, db)

    if result is None:
        raise HTTPException(status_code=404, detail="Cant get exercise")

    data.name_exercises = result
    return data
