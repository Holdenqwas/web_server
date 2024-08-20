import os
from datetime import timedelta


from fastapi import APIRouter, Response, HTTPException
from fastapi.params import Depends
from fastapi.security import OAuth2PasswordRequestForm

from ..utils.auth import generate_token

router = APIRouter()
ACCESS_TOKEN_EXPIRED_IN = int(os.getenv("EXPIRED_IN"))

@router.post("/token")
async def login(payload: OAuth2PasswordRequestForm = Depends(), response: Response = None):
    if os.getenv('IS_NEED_GENERATE_TOKEN', 'False') == 'True':
        # need verify payload
        access_token = generate_token(payload.username, timedelta(
            minutes=ACCESS_TOKEN_EXPIRED_IN))

        response.set_cookie("access_token", access_token,
                            ACCESS_TOKEN_EXPIRED_IN * 60,
                            ACCESS_TOKEN_EXPIRED_IN * 60,
                            "/", None, False, True, "lax")
        return {"access_token": access_token, "token_type": "bearer"}

    raise HTTPException(status_code=403, detail="Invalid token")

