from sqlalchemy import select, UUID, update
from sqlalchemy.ext.asyncio import AsyncSession
from app.crud.users import get_user
from app.models import db_model


async def user_add_shop_list(username: str, uid: UUID, db: AsyncSession):
    user = await get_user(username, db)
    if user:
        if user.array_shop_list and len(user.array_shop_list):
            arr = set(user.array_shop_list)
            arr.add(uid)

            stmt = (
                update(db_model.Users)
                .values(array_shop_list=list(arr))
                .where(db_model.Users.user_name == username)
            )
            await db.execute(stmt)
        else:
            user.array_shop_list = [uid]
        return user
    return None


async def get_shop_list(username: str, name: str, db: AsyncSession):
    user = await get_user(username, db)

    stmt = select(db_model.ShopList).where(
        db_model.ShopList.uid.in_(user.array_shop_list),
        db_model.ShopList.name == name,
    )
    result = await db.execute(stmt)
    if result:
        db_data = result.scalars().first()
        return db_data
    return None


async def get_uid_shop_list(username: str, name: str, db: AsyncSession):
    shop_list = await get_shop_list(username, name, db)
    return shop_list.uid


async def create_shop_list(username: str, name: str, db: AsyncSession):
    new_list = db_model.ShopList(name=name, array_username=[username])
    db.add(new_list)
    await db.commit()
    await db.refresh(new_list)

    user = await user_add_shop_list(username, new_list.uid, db)
    if user:
        return new_list
    return None


async def delete_shop_list(username: str, name: str, db: AsyncSession):
    shop_list = await get_shop_list(username, name, db)
    user = await get_user(username, db)
    if user:
        user.array_shop_list = [
            uid for uid in user.array_shop_list if uid != shop_list.uid
        ]
        db.add(user)

    if shop_list:
        if len(shop_list.array_username) == 1:
            await db.delete(shop_list)
        else:
            shop_list.array_username = [
                item for item in shop_list.array_username if item != username
            ]
            db.add(shop_list)
    return user


async def add_items_to_shop_list(
    username: str, name: str, items: str, db: AsyncSession
):
    shop_list = await get_shop_list(username, name, db)

    if shop_list and items:
        items = items.split("\n")
        if shop_list.items:
            new_arr_items = list(set(shop_list.items + items))
        else:
            new_arr_items = list(set(items))
        new_arr_items.sort()
        shop_list.items = new_arr_items

        db.add(shop_list)

        return shop_list


async def del_item_to_shop_list(
    username: str, name: str, item: str, db: AsyncSession
):
    shop_list = await get_shop_list(username, name, db)
    if shop_list:
        shop_list.items = [val for val in shop_list.items if val != item]
        db.add(shop_list)

        return shop_list
