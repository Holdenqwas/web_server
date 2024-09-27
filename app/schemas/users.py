from pydantic import BaseModel, Field
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

class NameExercise(BaseSchema):
    user_name: str
    names: str
    name_train: str

class User(BaseSchema):
    name: str
    last_date_license: Optional[datetime] = None
    name_trainings = str
    name_exer_train1 = str
    name_exer_train2 = str
    name_exer_train3 = str
    name_exer_train4 = str
    name_exer_train5 = str