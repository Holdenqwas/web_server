from sqlalchemy import select, UUID, update, and_
from sqlalchemy.ext.asyncio import AsyncSession
from app.crud.users import get_user
from app.models import db_model


async def user_add_shop_list(user_id: str, uid: UUID, db: AsyncSession):
    user = await get_user(user_id, db)
    if user:
        if user.array_shop_list and len(user.array_shop_list):
            arr = set(user.array_shop_list)
            arr.add(uid)

            stmt = (
                update(db_model.Users)
                .values(array_shop_list=list(arr))
                .where(db_model.Users.user_id == user_id)
            )
            await db.execute(stmt)
        else:
            user.array_shop_list = [uid]

        stmt = select(db_model.ShopList).where(db_model.ShopList.uid == uid)
        result = await db.execute(stmt)
        db_data = result.scalars().first()

        arr_users = set(db_data.array_user_id)
        arr_users.add(user_id)

        stmt = (
            update(db_model.ShopList)
            .values(array_user_id=list(arr_users))
            .where(db_model.ShopList.uid == uid)
        )
        await db.execute(stmt)
        return user
    return None


async def get_names_shop_list(user_id: str, db: AsyncSession):
    user = await get_user(user_id, db)

    if user.array_shop_list:
        stmt = select(db_model.ShopList).where(
            db_model.ShopList.uid.in_(user.array_shop_list)
        )
        result = await db.execute(stmt)
        db_data = result.scalars().all()
        return [item.name for item in db_data]
    return None


async def get_shop_list(user_id: str, name: str, db: AsyncSession):
    user = await get_user(user_id, db)
    stmt = select(db_model.ShopList).where(
        and_(
            db_model.ShopList.uid.in_(user.array_shop_list),
            db_model.ShopList.name == name,
        )
    )
    result = await db.execute(stmt)

    if result:
        db_data = result.scalars().first()
        return db_data
    return None


async def get_uid_shop_list(user_id: str, name: str, db: AsyncSession):
    shop_list = await get_shop_list(user_id, name, db)
    return shop_list.uid


async def create_shop_list(user_id: str, name: str, db: AsyncSession):
    new_list = db_model.ShopList(name=name, array_user_id=[user_id])
    db.add(new_list)
    await db.commit()
    await db.refresh(new_list)

    user = await user_add_shop_list(user_id, new_list.uid, db)
    if user:
        return new_list
    return None


async def delete_shop_list(user_id: str, name: str, db: AsyncSession):
    shop_list = await get_shop_list(user_id, name, db)
    user = await get_user(user_id, db)
    if user:
        user.array_shop_list = [
            uid for uid in user.array_shop_list if uid != shop_list.uid
        ]
        db.add(user)

    if shop_list:
        if len(shop_list.array_user_id) == 1:
            await db.delete(shop_list)
        else:
            shop_list.array_user_id = [
                item for item in shop_list.array_user_id if item != user_id
            ]
            db.add(shop_list)
    return user


async def add_items_to_shop_list(
    user_id: str, name: str, items: str, db: AsyncSession
):
    shop_list = await get_shop_list(user_id, name, db)

    if shop_list and items:
        items = [item.strip() for item in items.split("\n")]
        if shop_list.items:
            new_arr_items = list(set(shop_list.items + items))
        else:
            new_arr_items = list(set(items))
        new_arr_items.sort()
        shop_list.items = new_arr_items

        db.add(shop_list)

        return shop_list


async def del_item_to_shop_list(
    user_id: str, name: str, item: str, db: AsyncSession
):
    shop_list = await get_shop_list(user_id, name, db)

    if shop_list:
        shop_list.items = [val for val in shop_list.items if val != item]
        db.add(shop_list)

        return shop_list
