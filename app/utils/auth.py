from datetime import timedelta, datetime

import jwt
import os
from fastapi import Depends, HTTPException
from app.schemas.auth import Oauth2Scheme


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
    except:
        return None


def generate_token(user_id: str, timedelta_for_expiration=timedelta(days=1)):
    expiration = datetime.utcnow() + timedelta_for_expiration
    encoded_jwt = jwt.encode(
        {"exp": expiration, "scopes": user_id},
        os.getenv("JWT_KEY"),
        algorithm="HS256",
    )
    if isinstance(encoded_jwt, bytes):
        encoded_jwt = encoded_jwt.decode("utf-8")

    return encoded_jwt


def decode_token(token: str):
    try:
        jwt.decode(token, options={"verify_signature": False})
    except jwt.ExpiredSignatureError:
        return None


async def require_user(token: str = Depends(Oauth2Scheme)):
    user_id = verify_token_service(token)

    if not user_id:
        raise HTTPException(status_code=403, detail="Invalid token")

    return user_id
