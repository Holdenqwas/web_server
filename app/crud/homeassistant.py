import json
import logging
from typing import List

from sqlalchemy.ext.asyncio import AsyncSession

from app.schemas import homeassistant as schemas
from app.models import db_model


async def write_light_activity(data: List[str | None], db: AsyncSession):
    new_items = []

    for item in data:
        try:
            new_record_raw = json.loads(item)
            new_record = db_model.HomeActivity(**new_record_raw)
            new_items.append(new_record)
        except Exception as e:
            logging.error(f"Не смог распарсить и создать HomeActivity. {e.args}")

    if not new_items:
        return schemas.Message(success=False, message="Нет элементов, которые можно записать")
    
    db.add_all(new_items)

    return schemas.Message(success=True, message="Записано")