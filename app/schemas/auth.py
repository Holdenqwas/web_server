from fastapi.security import OAuth2PasswordBearer


from app.schemas.shared import BaseSchema

Oauth2Scheme = OAuth2PasswordBearer(tokenUrl="/token_for_services")


class AuthDTO(BaseSchema):
    user_id: str
    verify_code: str
    state: str
    client_id: str
    scope: str
