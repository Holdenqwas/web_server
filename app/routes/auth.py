import os
from fastapi.responses import RedirectResponse
import requests
import urllib.parse

from datetime import timedelta
from fastapi import APIRouter, Form, Request, Response, HTTPException, Body
from fastapi.params import Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud import auth as crud
from app.crud.ver_code import verify_code
from app.schemas import auth as schemas
from app.utils.auth import decode_token, generate_token
from app.utils.database import get_db


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


@router.post("/create_token")
async def create_token(
    grant_type: str = Form(...),
    code: str = Form(...),
    db: AsyncSession = Depends(get_db),
):
    print("code", code)
    if grant_type != "authorization_code":
        raise HTTPException(status_code=400, detail="Unsupported grant type")

    ver_code = await verify_code(code, db)
    if not ver_code:
        raise HTTPException(403, "Код недействителен")

    access_token = generate_token(ver_code.user_id, timedelta(seconds=600))
    refresh_token = generate_token(
        ver_code.user_id, timedelta(seconds=86400 * 30)
    )

    return {
        "access_token": access_token,
        "refresh_token": refresh_token,
        "expires_in": 600,
        "token_type": "bearer",
    }


@router.post("/refresh_token")
async def refresh_token(
    grant_type: str = Form(...), refresh_token: str = Form(...)
):
    print("refresh_token", refresh_token)
    if grant_type != "refresh_token":
        raise HTTPException(status_code=400, detail="Unsupported grant type")
    user_id = decode_token(refresh_token)

    if not user_id:
        HTTPException(403, "Рефреш токен не валиден")

    access_token = generate_token(user_id, timedelta(seconds=600))
    refresh_token = generate_token(user_id, timedelta(seconds=86400 * 30))

    return {
        "access_token": access_token,
        "refresh_token": refresh_token,
        "expires_in": 600,
        "token_type": "bearer",
    }


@router.post("/login")
async def login(
    payload: schemas.AuthDTO,
    db: AsyncSession = Depends(get_db),
):
    code = await crud.verify_auth(payload, db)
    if code:
        headers = (
            {
                "Access-Control-Allow-Headers": "Content-Type",
                "Access-Control-Allow-Origin": "*",
                "Content-Type": "application/json",
                "Access-Control-Allow-Methods": "OPTIONS,POST,GET,PATCH",
            },
        )
        redirect_url = (
            f"https://social.yandex.net/broker/redirect?"
            f"client_id={payload.client_id}&state={payload.state}&code={code}&scope={payload.scope}"
        )

        return RedirectResponse(url=redirect_url, status_code=302)
    else:
        raise HTTPException(status_code=404, headers=headers, detail="Что-то пошло не так")


# @router.get("/generate_verify_code")
# async def generate_verify_code(
#     user_id: int,
#     db: AsyncSession = Depends(get_db),
# ):
#     await crud.generate_verify_code(user_id, db)
