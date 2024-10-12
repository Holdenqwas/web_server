from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import APIRouter, HTTPException, Path, Depends, Query
from typing import Union
from pydantic import UUID4

from app.utils.database import get_db
from app.utils.auth import require_user
from app.crud import shop_list as crud
from app.schemas.users import User
from app.schemas import shop_list as shemas_shop

router = APIRouter()


@router.post("/user_add_shop_list", response_model=User)
async def add_user(
    data: shemas_shop.AttachShopList,
    # user: str = Depends(require_user),
    db: AsyncSession = Depends(get_db),
):
    return await crud.user_add_shop_list(data.username, data.uid, db)


@router.get("/get_names_shop_list", response_model=shemas_shop.NamesShopList)
async def get_names_all_shop_list_for_user(
    username: str = Query(default="string"),
    # user: str = Depends(require_user),
    db: AsyncSession = Depends(get_db),
):
    names = await crud.get_names_shop_list(username, db)
    return shemas_shop.NamesShopList(names=names)


@router.get("/get_shop_list", response_model=shemas_shop.ShopListDTO)
async def get_shop_list(
    username: str = Query(default="string"),
    name: str = Query(default="Общий"),
    # user: str = Depends(require_user),
    db: AsyncSession = Depends(get_db),
):
    return await crud.get_shop_list(username, name, db)


@router.get("/get_uid_shop_list", response_model=UUID4)
async def get_shop_list(
    username: str = Query(default="string"),
    name: str = Query(default="Общий"),
    # user: str = Depends(require_user),
    db: AsyncSession = Depends(get_db),
):
    return await crud.get_uid_shop_list(username, name, db)


@router.post("/create_shop_list", response_model=shemas_shop.ShopListDTO)
async def create_shop_list(
    data: shemas_shop.CreateShopList,
    # user: str = Depends(require_user),
    db: AsyncSession = Depends(get_db),
):
    return await crud.create_shop_list(data.username, data.name, db)


@router.delete("/delete_shop_list", response_model=User)
async def delete_shop_list(
    username: str = Query(default="string"),
    name: str = Query(default="Общий"),
    # user: str = Depends(require_user),
    db: AsyncSession = Depends(get_db),
):
    return await crud.delete_shop_list(username, name, db)


@router.post("/add_items_to_shop_list", response_model=shemas_shop.ShopListDTO)
async def add_items_to_shop_list(
    data: shemas_shop.AddItems,
    # user: str = Depends(require_user),
    db: AsyncSession = Depends(get_db),
):
    return await crud.add_items_to_shop_list(
        data.username, data.name, data.items, db
    )


@router.delete("/del_item_from_shop_list", response_model=shemas_shop.ShopListDTO)
async def del_item_from_shop_list(
    username: str = Query(default="string"),
    name: str = Query(default="Общий"),
    item: str = Query(default="Молоко"),
    # user: str = Depends(require_user),
    db: AsyncSession = Depends(get_db),
):
    
    return await crud.del_item_to_shop_list(
        username, name, item, db
    )
