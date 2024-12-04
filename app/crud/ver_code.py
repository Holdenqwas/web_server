import time
import uuid
from sqlalchemy import and_, select, delete
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas import users as schema
from app.models import db_model


async def verify_code(code: str, db: AsyncSession):
    stmt = select(db_model.VerCode).where(and_(db_model.VerCode.expires_at >  int(time.time()), db_model.VerCode.code == code))
    result = await db.execute(stmt)

    db_data = result.scalars().first()
    return db_data


async def create_code(user_uid: str, db: AsyncSession):
    code = str(uuid.uuid4())
    expires_at = int(time.time()) + 600  # Код действителен 10 минут

    new_code = db_model.Users(user_uid=user_uid, code=code, expires_at=expires_at)
    db.add(new_code)
    return code

