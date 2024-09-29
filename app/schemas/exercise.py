from pydantic import Field

from app.schemas.shared import BaseSchema


class ExerciseDTO(BaseSchema):
    user_name: str
    name_training: str = Field(examples=["breast"])
    name_exercise: str = Field(examples=["Жим"])
    value: float = Field(examples=[30.0])
