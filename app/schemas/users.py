from datetime import datetime
from typing import Optional

from app.schemas.shared import BaseSchema


class CreateUser(BaseSchema):
    user_name: str
    last_date_license: Optional[datetime] = None


class UpdateDateLicense(BaseSchema):
    user_name: str
    last_date_license: datetime


class NameTrainings(BaseSchema):
    user_name: str
    names: str


class NameExercises(BaseSchema):
    user_name: str
    names: str
    name_train: str


class User(BaseSchema):
    user_name: str
    allow_access: bool
    last_date_license: Optional[datetime] = None
    name_trainings: str | None
    name_exer_train1: str | None
    name_exer_train2: str | None
    name_exer_train3: str | None
    name_exer_train4: str | None
    name_exer_train5: str | None
