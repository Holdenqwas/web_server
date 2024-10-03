from sqlalchemy import select, and_
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from app.schemas import training as schema
from app.models import db_model
from .users import get_user


async def get_name_trains(user_name: str, db: AsyncSession) -> List[str]:
    user = await get_user(user_name, db)
    name_trains = user.name_trainings.split(",")
    return name_trains


async def get_name_exercise(data: schema.NameExercises, db: AsyncSession):
    user = await get_user(data.user_name, db)

    name_trains = await get_name_trains(data.user_name, db)
    index_trains = name_trains.index(data.name_training) + 1

    raw_names = getattr(user, f"name_exer_train{index_trains}")
    name_exercises = raw_names.split(",")
    return name_exercises


async def get_index_train_and_exercise(
    user_name: str, name_train: str, name_exercise: str, db: AsyncSession
):
    user = await get_user(user_name, db)

    name_trains = user.name_trainings.split(",")
    index_train = name_trains.index(name_train) + 1

    raw_names = getattr(user, f"name_exer_train{index_train}")
    name_exercises = raw_names.split(",")
    index_exer = name_exercises.index(name_exercise) + 1
    return index_train, index_exer


async def get_training(user_name: str, db: AsyncSession):
    stmt = (
        select(db_model.TrainingAll)
        .where(db_model.TrainingAll.user_name == user_name)
        .order_by(db_model.TrainingAll.date.desc())
    )
    result = await db.execute(stmt)
    db_data = result.scalars().first()
    return db_data


async def get_prev_training(user_name: str, index_train, db: AsyncSession):
    stmt = (
        select(db_model.TrainingAll)
        .where(
            and_(
                db_model.TrainingAll.user_name == user_name,
                db_model.TrainingAll.index_train == index_train
            )
        )
        .order_by(db_model.TrainingAll.date.desc())
        .limit(2)
    )
    result = await db.execute(stmt)
    db_data = result.scalars().all()
    if len(db_data) == 2:
        return db_data[1]
    return


async def create_training_all(data: schema.CreateTrainingAll, db: AsyncSession):
    new_train = db_model.TrainingAll(**data.model_dump())
    db.add(new_train)
    new_train.name_trains = await get_name_trains(data.user_name, db)
    return new_train


async def create_train(data: schema.CreateTrain, db: AsyncSession):
    name_trains = await get_name_trains(data.user_name, db)
    index_trains = name_trains.index(data.name_training) + 1

    train_model = db_model.get_model(f"train{index_trains}")
    new_train = train_model()
    db.add(new_train)
    await db.refresh(new_train)

    train_all = await get_training(data.user_name, db)

    train_all.index_train = index_trains
    setattr(train_all, f"train{index_trains}_uid", new_train.uid)
    db.add(train_all)
    return train_all
