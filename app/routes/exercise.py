from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud import exercise as crud
from app.schemas import exercise as exercise_schema
from app.utils.auth import require_token_service
from app.utils.database import get_db


router = APIRouter()


@router.post("/write_exercise")
async def write_exercise(
    data: exercise_schema.ExerciseDTO,
    token: str = Depends(require_token_service),
    db: AsyncSession = Depends(get_db),
):
    await crud.write_exercise(data, db)


@router.post("/last_exercise")
async def get_last_exercise(
    data: exercise_schema.ExerciseBase,
    token: str = Depends(require_token_service),
    db: AsyncSession = Depends(get_db),
):
    return await crud.get_last_exercise(
        data.user_id, data.name_training, data.name_exercise, db
    )
