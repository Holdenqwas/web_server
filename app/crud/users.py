import sys
from sqlalchemy import select, delete
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas import users as schema
from app.models import db_model


async def get_user(user_name: str, db: AsyncSession):
    stmt = select(db_model.Users).where(db_model.Users.name == user_name)
    result = await db.execute(stmt)
    if result:
        db_data = result.scalars().first()
        return db_data
    return None


async def create_user(data: schema.CreateUser, db: AsyncSession):
    user = get_user(data.user_name, db)
    if user:
        return user
    
    new_user = db_model.Users(**data.model_dump())
    new_user.allow_access = True
    db.add(new_user)
    return new_user


async def update_date_license(data: schema.UpdateDateLicense, db: AsyncSession):
    user = await get_user(data.user_name, db)
    if user:
        user.last_date_license = data.last_date_license
        db.add(user)
    return user


async def update_name_trainings(data: schema.NameTrainings, db: AsyncSession):
    user = await get_user(data.user_name, db)
    if user:
        user.name_trainings = data.names
        db.add(user)
    return user


async def delete_trainings(user_name: str, db: AsyncSession):
    user = await get_user(user_name, db)
    if user:
        stmt = delete(db_model.TrainingAll).where(db_model.TrainingAll.name == user_name)
        await db.execute(stmt)
        user.name_trainings = ""
        user.name_exer_train1 = ""
        user.name_exer_train2 = ""
        user.name_exer_train1 = ""
        user.name_exer_train1 = ""
        user.name_exer_train1 = ""
        db.add(user)
    return user



async def update_name_trainings(data: schema.NameTrainings, db: AsyncSession):
    user = await get_user(data.user_name, db)
    if user:
        user.name_trainings = data.names
        db.add(user)
    return user


###############
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