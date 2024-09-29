from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas import exercise as schema
from app.models import db_model
from .users import get_user
from .training import get_training


async def write_exercise(data: schema.ExerciseDTO, db: AsyncSession):
    train = await get_training(data.user_name, db)
    uid = getattr(train, f"train{train.index_train}_uid")
    model = db_model.get_model(f"train{train.index_train}")

    user = await get_user(data.user_name, db)
    name_exercise = getattr(user, f"name_exer_train{train.index_train}").split(
        ","
    )
    index_exercise = name_exercise.index(data.name_exercise) + 1

    stmt = select(model).filter(model.uid == uid)
    result = await db.execute(stmt)
    db_data = result.scalars().first()

    setattr(db_data, f"ex{index_exercise}", data.value)
    db.add(db_data)
    return train
