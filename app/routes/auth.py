import os
import requests
from datetime import timedelta

from fastapi import APIRouter, Response, HTTPException
from fastapi.params import Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession

from app.schemas.auth import AuthDTO
from app.utils.auth import generate_token
from app.utils.database import get_db
from app.crud import auth as crud


router = APIRouter()
ACCESS_TOKEN_EXPIRED_IN = int(os.getenv("EXPIRED_IN"))


@router.post("/token_for_services")
async def token(
    payload: OAuth2PasswordRequestForm = Depends(), response: Response = None
):
    if os.getenv("IS_NEED_GENERATE_TOKEN", "False") == "True":
        # need verify payload
        access_token = generate_token(
            payload.user_id, timedelta(minutes=ACCESS_TOKEN_EXPIRED_IN)
        )

        response.set_cookie(
            "access_token",
            access_token,
            ACCESS_TOKEN_EXPIRED_IN * 60,
            ACCESS_TOKEN_EXPIRED_IN * 60,
            "/",
            None,
            False,
            True,
            "lax",
        )
        return {"access_token": access_token, "token_type": "bearer"}

    raise HTTPException(
        status_code=403, detail="Generate token for services disabled"
    )


@router.get("/create_token")
async def create_token(code: str):
    expires_in = 86400
    access_token = generate_token(code, timedelta(seconds=expires_in))
    refresh_token = generate_token(code, timedelta(seconds=expires_in * 30))

    return {
        "access_token": access_token,
        "refresh_token": refresh_token,
        "expires_in": expires_in,
        "token_type": "bearer",
    }


@router.get("/refresh_token")
async def refresh_token(code: str):
    expires_in = 86400
    access_token = generate_token(code, timedelta(seconds=expires_in))
    refresh_token = generate_token(code, timedelta(seconds=expires_in * 30))

    return {
        "access_token": access_token,
        "refresh_token": refresh_token,
        "expires_in": expires_in,
        "token_type": "bearer",
    }


@router.post("/login")
async def login(
    payload: AuthDTO,
    db: AsyncSession = Depends(get_db),
):
    code = await crud.verify_auth(payload, db)
    if code:
        params = {
            "code": code,
            "state": payload.state,
            "client_id": payload.client_id,
            "scope": payload.scope,
        }

        print(params)
        res = requests.request(
            "GET",
            url="https://social.yandex.net/broker/redirect",
            params=params,
        )
        print(res.status_code, res.text)
    else:
        raise HTTPException(status_code=404, detail="Что-то пошло не так")


# @router.get("/generate_verify_code")
# async def generate_verify_code(
#     user_id: int,
#     db: AsyncSession = Depends(get_db),
# ):
#     await crud.generate_verify_code(user_id, db)
