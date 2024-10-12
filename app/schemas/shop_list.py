from pydantic import Field, UUID4
from datetime import datetime
from typing import Optional, List

from app.schemas.shared import BaseSchema



class ShopListDTO(BaseSchema):
    array_username: List[str]
    name: str
    items: Optional[List[str]] = None
    update_time: datetime



class NamesShopList(BaseSchema):
    names: Optional[List[str]] = None


class CreateShopList(BaseSchema):
    username: str
    name: str


class AttachShopList(BaseSchema):
    username: str
    uid: UUID4


class DelItem(BaseSchema):
    username: str
    name: str
    item: str


class AddItems(BaseSchema):
    username: str
    name: str
    items: str