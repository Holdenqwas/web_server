from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import APIRouter, Depends

from app.utils.database import get_db
from app.utils.auth import require_token_service
from app.crud import homeassistant as crud
from app.schemas import homeassistant as schemas

router = APIRouter()


@router.post("/write_light_activity") # , response_model=schemas.Message)
async def write_light_activity(
    body: schemas.LightActivityRecord,
    # token: str = Depends(require_token_service),
    db: AsyncSession = Depends(get_db),
):
    return await crud.write_light_activity(body.data, db)
