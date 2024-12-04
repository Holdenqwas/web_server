from fastapi.security import OAuth2PasswordBearer, OAuth2


from app.schemas.shared import BaseSchema

Oauth2SchemeServices = OAuth2PasswordBearer(tokenUrl="/token_for_services")
Oauth2Scheme = OAuth2(auto_error=False)


class AuthDTO(BaseSchema):
    user_id: str
    verify_code: str
    state: str
    client_id: str
    scope: str

class AuthRequestToken(BaseSchema):
    grant_type: str
    code: str
    redirect_uri: str
    client_id: str