from fastapi.security import OAuth2PasswordBearer


from app.schemas.shared import BaseSchema

Oauth2Scheme = OAuth2PasswordBearer(tokenUrl="/token_for_services")


class AuthDTO(BaseSchema):
    user_id: int
    verify_code: int
    state: str
    client_id: str
    scope: str
