from pydantic import Field
from typing import Optional

from app.schemas.shared import BaseSchema


class TrainingDTO(BaseSchema):
    user_name: str
    weight: Optional[float] = None


class CreateTrain(BaseSchema):
    user_name: str
    name_training: str = Field(examples=["breast"])
