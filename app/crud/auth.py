import random
from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.schemas import auth as schema
from .users import get_user


async def verify_auth(data: schema.AuthDTO, db: AsyncSession):
    user = await get_user(data.user_id, db)
    if not user:
        raise HTTPException(
            status_code=404, detail="Не возможно найти пользователя"
        )

    if not user.vefiry_code:
        raise HTTPException(
            status_code=404,
            detail="Верификационный код не сгенерирован, "
            + "выполните заново шаги из инструкции",
        )

    if user.user_id == data.user_id and user.vefiry_code == data.verify_code:
        user.vefiry_code = None
        return str(user.uid)

    raise HTTPException(
        status_code=404, detail="Значения не совпадают, проверьте данные"
    )


async def generate_verify_code(data: schema.AuthDTO, db: AsyncSession):
    user = await get_user(data.user_id, db)
    if not user:
        raise HTTPException(status_code=404, detail="Cant find user")

    user.vefiry_code = round(random.random() * 100_000)
