import random
from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.schemas import auth as schema
from app.crud.shop_list import get_uid_shop_list
from .users import get_user


async def verify_auth(data: schema.AuthDTO, db: AsyncSession):
    try:
        data.user_id = int(data.user_id)
    except ValueError:
        raise HTTPException(
            status_code=404, detail="Первое число должно содержать только числа"
        )
    
    try:
        data.verify_code = int(data.verify_code)
    except ValueError:
        raise HTTPException(
            status_code=404, detail="Второе число должно содержать только числа"
        )

    user = await get_user(data.user_id, db)
    print(user)
    if not user:
        raise HTTPException(
            status_code=404, detail="Введено неправильное первое число"
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


async def generate_verify_code(
    user_id: int, shop_list_name: str, db: AsyncSession
):
    user = await get_user(user_id, db)
    if not user:
        raise HTTPException(status_code=404, detail="Cant find user")

    code = round(random.random() * 1_000_000)
    while code == 1_000_000:
        code = round(random.random() * 1_000_000)

    user.vefiry_code = code

    shop_list_uid = await get_uid_shop_list(user_id, shop_list_name, db)
    user.default_shop_list_uid = shop_list_uid
    db.add(user)
    return user
