from pydantic import Field

from app.schemas.shared import BaseSchema


class ExerciseBase(BaseSchema):
    user_id: int
    name_training: str = Field(examples=["breast"])
    name_exercise: str = Field(examples=["Жим"])


class ExerciseDTO(ExerciseBase):
    value: float = Field(examples=[30.0])
