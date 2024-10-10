from sqlalchemy import select, UUID
from sqlalchemy.ext.asyncio import AsyncSession
from app.crud.users import get_user
from app.models import db_model


async def user_add_shop_list(username: str, uid: UUID, db: AsyncSession):
    user = await get_user(username, db)
    if user:
        user.array_shop_list.append(uid)
        db.add(user)
        return user
    return None


async def get_shop_list(username: str, name: str, db: AsyncSession):
    user = await get_user(username, db)

    stmt = select(db_model.ShopList).where(
        db_model.ShopList.uid in user.array_shop_list,
        db_model.ShopList.name == name,
    )
    result = await db.execute(stmt)
    if result:
        db_data = result.scalars().first()
        return db_data
    return None


async def get_uid_shop_list(username: str, name: str, db: AsyncSession):
    shop_list = await get_shop_list(username, name)
    return shop_list.uid


async def create_shop_list(username: str, name: str, db: AsyncSession):
    new_list = db_model.ShopList(name=name, array_username=[username], items=[])
    db.add(new_list)

    user = await user_add_shop_list(username, new_list.uid, db)
    if user:
        return new_list
    return None


async def delete_shop_list(username: str, name: str, db: AsyncSession):
    shop_list = await get_shop_list(username, name)
    user = await get_user(username, db)
    if user:
        user.array_shop_list = [
            uid for uid in user.array_shop_list if uid != shop_list.uid
        ]
        db.add(user)

    if shop_list:
        if len(shop_list) == 1:
            db.delete(shop_list)
        else:
            shop_list.array_username = [
                item for item in shop_list.array_username if item != username
            ]
            db.add(shop_list)
    return user


async def add_items_to_shop_list(
    username: str, name: str, items: str, db: AsyncSession
):
    shop_list = await get_shop_list(username, name)

    if shop_list and items:
        items = items.split("\n")
        new_arr_items = set(shop_list + items)
        new_arr_items.sort()
        shop_list.items = new_arr_items
        db.add(new_arr_items)

        return shop_list


async def del_item_to_shop_list(
    username: str, name: str, item: str, db: AsyncSession
):
    shop_list = await get_shop_list(username, name)

    if shop_list:
        shop_list.items = [val for val in shop_list.items if val != item]
        db.add(shop_list)

        return shop_list
