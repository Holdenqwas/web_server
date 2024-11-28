from pydantic import Field
from typing import Optional, List

from app.schemas.shared import BaseSchema


class NameTrainingsDTO(BaseSchema):
    name_trains: Optional[List[str]] = None


class CreateTrainingAll(BaseSchema):
    user_id: int
    weight: Optional[float] = None


class TrainingDTO(BaseSchema):
    user_id: int
    weight: Optional[float] = None
    name_trains: Optional[List[str]] = None


class CreateTrain(BaseSchema):
    user_id: int
    name_training: str = Field(examples=["breast"])


class NameExercises(BaseSchema):
    user_id: int
    name_training: str
    name_exercises: Optional[List[str]] = str
