from pydantic import Field, UUID4
from typing import Optional, List

from app.schemas.shared import BaseSchema



class ShopListDTO(BaseSchema):
    username: str
    name: str
    items: Optional[List[str]] = None


class AttachShopList(BaseSchema):
    username: str
    uid: UUID4


class DelItem(BaseSchema):
    username: str
    name: str
    item: str
