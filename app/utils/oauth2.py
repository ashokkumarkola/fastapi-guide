from datetime import datetime, timedelta, timezone
from typing import Annotated

from jose import jwt
from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
# from jwt.exceptions import InvalidTokenError
# from pwdlib import PasswordHash
# from pydantic import BaseModel

from app.utils.token import verify_token

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login") # /auth/login

def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    
    return verify_token(token, credentials_exception)


