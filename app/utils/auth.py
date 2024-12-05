from datetime import timedelta, datetime

import jwt
import os
from fastapi import Depends, HTTPException
from app.schemas.auth import Oauth2SchemeServices, Oauth2Scheme


def verify_token_service(token: str):
    try:
        jwt_options = {
            "verify_signature": True,
            "verify_exp": True,
            "verify_nbf": False,
            "verify_iat": False,
            "verify_aud": False,
        }
        decoded = jwt.decode(
            token,
            key=os.getenv("JWT_KEY"),
            algorithms=[
                "HS256",
            ],
            options=jwt_options,
        )

        if decoded["scopes"] != os.getenv("MY_NAME"):
            return None
        return decoded["scopes"]
    except Exception as e:
        print(e.args)
        return None


def generate_token(user_id: int, timedelta_for_expiration=timedelta(days=1)) -> str:

    expiration = datetime.utcnow() + timedelta_for_expiration
    encoded_jwt = jwt.encode(
        {"exp": expiration, "sub": str(user_id)},
        os.getenv("JWT_KEY"),
        algorithm="HS256",
    )
    if isinstance(encoded_jwt, bytes):
        encoded_jwt = encoded_jwt.decode("utf-8")

    return encoded_jwt


def decode_token(token: str = Depends(Oauth2Scheme), need_format: bool = True) -> int | None:
    if not token: return None
    try:
        if need_format:
            token = token[7:]

        token = token.encode('utf-8')

        
        jwt_options = {
            "verify_signature": True,
            "verify_exp": True,
            "verify_nbf": False,
            "verify_iat": False,
            "verify_aud": False,
        }
        decoded = jwt.decode(
            token,
            key=os.getenv("JWT_KEY"),
            algorithms=[
                "HS256",
            ],
            options=jwt_options,
        )
        return int(decoded["sub"])
    except Exception as e:
        print(e.args)
        return None


async def require_token_service(token: str = Depends(Oauth2SchemeServices)):
    user_id = verify_token_service(token)

    if not user_id:
        raise HTTPException(status_code=403, detail="Invalid token")

    return user_id
