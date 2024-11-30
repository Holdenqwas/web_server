from datetime import datetime
from pydantic import UUID4
from typing import Optional, List

from app.schemas.shared import BaseSchema


class CreateUser(BaseSchema):
    user_id: int
    username: Optional[str] = None
    last_date_license: Optional[datetime] = None


class UpdateDateLicense(BaseSchema):
    user_id: int
    last_date_license: datetime


class NameTrainings(BaseSchema):
    user_id: int
    names: str


class NameExercises(BaseSchema):
    user_id: int
    names: str
    name_train: str


class User(BaseSchema):
    user_id: int
    allow_access: bool
    last_date_license: Optional[datetime] = None
    name_trainings: str | None
    name_exer_train1: str | None
    name_exer_train2: str | None
    name_exer_train3: str | None
    name_exer_train4: str | None
    name_exer_train5: str | None
    array_shop_list: List[UUID4] | None


class VerificateCode(BaseSchema):
    code: int
