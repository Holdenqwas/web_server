from fastapi.security import OAuth2PasswordBearer

Oauth2Scheme = OAuth2PasswordBearer(tokenUrl="/token")