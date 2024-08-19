import sys
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemes import training as schema
from app.models import db_model


match_name_menu_table = {"train_breast_menu": "breast",
                         "train_beak_menu": "beak",
                         "train_leg_menu": "leg"}

match_exercise_column = {"Жим": "bench_press", "Нак": "bench_press_inclined",
                         "Пул": "pullover", "Гант": "dumbbells", "Блок": "block",
                         "ЖимТ": "triceps_bench_press", "Фран": "french_bench_press",
                         "Гиря": "kettlebell", "Грав": "gravitron", "Верх": "upper_block",
                         "Низ": "lower_block", "Стоя": "army_bench_press",
                         "Подбородок": "craving_for_chin", "Сидя": "head_press", "Присяд": "knee_bend",
                         "Платформа": "platform_press", "Разгибание": "extension_of_block"
}

async def get_training(db: AsyncSession):
    stmt = select(db_model.Training).order_by(db_model.Training.date.desc())
    result = await db.execute(stmt)
    db_data = result.scalars().first()
    return db_data


async def get_last_exercise(name_training: str, name_exercise: str, db: AsyncSession):
    train = await get_training(db)
    model = db_model.get_model(match_name_menu_table[name_training])

    if not train.breast_uid and not train.beak_uid and not train.leg_uid:
        stmt = select(model).order_by(model.date.desc())
        result = await db.execute(stmt)
        db_exercise = result.scalars().first()
        return getattr(db_exercise, match_exercise_column[name_exercise])

    stmt = select(model).order_by(model.date.desc()).limit(2)
    result = await db.execute(stmt)
    db_exercises = result.scalars().all()
    if len(db_exercises) == 2:
        return getattr(db_exercises[-1], match_exercise_column[name_exercise])
    return -1


async def create_training(data: schema.TrainingDTO, db: AsyncSession):
    new_train = db_model.Training(**data.model_dump())
    new_train.name_training = match_name_menu_table[data.name_training]
    db.add(new_train)
    return new_train


async def update_training(data: schema.TrainingDTO, db: AsyncSession):
    train = await get_training(db)
    if train:
        update_data = data.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            setattr(train, key, value)
        db.add(train)
    return train


async def write_exercise(data: schema.ExerciseDTO, db: AsyncSession):
    train = await get_training(db)
    if not train.breast_uid and not train.beak_uid and not train.leg_uid:
        # train.name_training = match_name_menu_table[data.name_training]
        model = db_model.get_model(match_name_menu_table[data.name_training])
        value = {match_exercise_column[data.name_exercise]: data.value}
        new_exercise = model(**value)
        db.add(new_exercise)
        stmt = select(model).order_by(model.date.desc())
        result = await db.execute(stmt)
        db_exercise = result.scalars().first()

        train.name_training = match_name_menu_table[data.name_training]
        setattr(train, train.name_training + "_uid", db_exercise.uid)
        db.add(train)
    else:
        uid = getattr(train, train.name_training + "_uid")
        model = db_model.get_model(train.name_training)

        stmt = select(model).filter(model.uid == uid)
        result = await db.execute(stmt)
        db_data = result.scalars().first()

        setattr(db_data, match_exercise_column[data.name_exercise], data.value)
        db.add(db_data)
    return train