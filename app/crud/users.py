from sqlalchemy import select, delete
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas import users as schema
from app.models import db_model


async def get_user(user_name: str, db: AsyncSession):
    stmt = select(db_model.Users).where(db_model.Users.user_name == user_name)
    result = await db.execute(stmt)
    if result:
        db_data = result.scalars().first()
        return db_data
    return None


async def create_user(data: schema.CreateUser, db: AsyncSession):
    user = await get_user(data.user_name, db)
    if user:
        return user

    new_user = db_model.Users(**data.model_dump(exclude_none=True))
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
        arr_names = [item.strip() for item in data.names.split(",")]
        if arr_names:
            user.name_trainings = ",".join(arr_names[:5])
        db.add(user)
    return user


async def delete_trainings(user_name: str, db: AsyncSession):
    user = await get_user(user_name, db)
    if user:
        stmt = delete(db_model.TrainingAll).where(
            db_model.TrainingAll.user_name == user_name
        )
        await db.execute(stmt)
        user.name_trainings = ""
        user.name_exer_train1 = ""
        user.name_exer_train2 = ""
        user.name_exer_train1 = ""
        user.name_exer_train1 = ""
        user.name_exer_train1 = ""
        db.add(user)
    return user


async def update_name_exercises(data: schema.NameExercises, db: AsyncSession):
    user = await get_user(data.user_name, db)
    if user:
        arr_names = [item.strip() for item in data.names.split(",")]
        name_trains = user.name_trainings.split(",")
        index_train = name_trains.index(data.name_train)
        if arr_names:
            setattr(
                user,
                f"name_exer_train{index_train+1}",
                ",".join(arr_names[:10]),
            )
        db.add(user)
    return user
