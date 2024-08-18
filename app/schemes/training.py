from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional

from app.schemes.shared import BaseSchema

class TrainingDTO(BaseSchema):
    weight: Optional[float] = None
    date: Optional[datetime] = None
    name_training: str = Field(examples=["breast"])


class BeakDTO(BaseSchema):
    triceps_bench_press: Optional[float] = None
    french_bench_press: Optional[float] = None
    kettlebell: Optional[float] = None
    gravitron: Optional[float] = None
    upper_block: Optional[float] = None
    lower_block: Optional[float] = None
    
    
class BreastDTO(BaseSchema):
    bench_press: Optional[float] = None
    bench_press_inclined: Optional[float] = None
    pullover: Optional[float] = None
    dumbbells: Optional[float] = None
    block: Optional[float] = None


class LegDTO(BaseSchema):
    army_bench_press: Optional[float] = None
    craving_for_chin: Optional[float] = None
    head_press: Optional[float] = None
    knee_bend: Optional[float] = None
    platform_press: Optional[float] = None
    extension_of_block: Optional[float] = None


class ExerciseDTO(BaseSchema):
    name_training: str = Field(examples=["train_breast_menu"])
    name_exercise: str = Field(examples=["Жим"])
    value: float = Field(examples=[30.0])