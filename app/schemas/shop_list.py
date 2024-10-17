from pydantic import Field, UUID4
from datetime import datetime
from typing import Optional, List

from app.schemas.shared import BaseSchema



class ShopListDTO(BaseSchema):
    array_user_id: List[int]
    name: str
    items: Optional[List[str]] = None
    update_time: datetime



class NamesShopList(BaseSchema):
    names: Optional[List[str]] = None


class CreateShopList(BaseSchema):
    user_id: int
    name: str


class AttachShopList(BaseSchema):
    user_id: int
    uid: UUID4


class DelItem(BaseSchema):
    user_id: int
    name: str
    item: str


class AddItems(BaseSchema):
    user_id: int
    name: str
    items: str