from pydantic import Field
from typing import Optional, List

from app.schemas.shared import BaseSchema


class CreateTrainingAll(BaseSchema):
    user_name: str
    weight: Optional[float] = None


class TrainingDTO(BaseSchema):
    user_name: str
    weight: Optional[float] = None
    name_trains: Optional[List[str]] = None


class CreateTrain(BaseSchema):
    user_name: str
    name_training: str = Field(examples=["breast"])


class NameExercises(BaseSchema):
    user_name: str
    name_training: str
    name_exercises: Optional[List[str]] = str
