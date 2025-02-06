from typing import List
from app.schemas.shared import BaseSchema


class LightActivityRecord(BaseSchema):
    data: List[str | None]


class Message(BaseSchema):
    success: bool = True
    message: str | None = None
