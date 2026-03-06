from datetime import datetime, timedelta, timezone
from typing import Dict, Any, Union, Dict, Optional, Annotated
from fastapi import HTTPException, status

from pwdlib import PasswordHash # Recommended hashing
# from pwdlib.hashers.argon2 import Argon2Hasher
# from pwdlib.hashers.bcrypt import BcryptHasher

import jwt  # PyJWT (recommended)
from jose import JWTError  # Fallback if needed; remove for pure PyJWT
from jwt.exceptions import InvalidTokenError  # PyJWT errors

from app.core.config import get_settings

settings = get_settings()

# -------- PASSWORD CONTEXTS -------- #

# Password hashing context
pwd_context = PasswordHash.recommended() # Argon2id (secure default)

# Modern password hashing with multiple algorithm support
# password_hash = PasswordHash([
#     Argon2Hasher(),  # Argon2 is the default (most secure)
#     BcryptHasher(),  # Fallback for legacy
# ])

# -------- Hashing Utilities -------- #
def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

# -------- Token Utilities -------- #
def create_token(data: dict, expires_delta: Union[timedelta, None] = None, refresh: bool = False) -> str:
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(
            minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES if not refresh else 0,  # 0 for calc
            days=settings.REFRESH_TOKEN_EXPIRE_DAYS if refresh else 0
        )
    if refresh:
        expire = datetime.now(timezone.utc) + timedelta(days=settings.REFRESH_TOKEN_EXPIRE_DAYS)
    to_encode.update({"exp": expire, "type": "refresh" if refresh else "access"})
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
    return encoded_jwt

def verify_and_decode_token(token: str) -> dict[str, Any]:
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        if payload.get("type") == "refresh":  # Distinguish for refresh logic
            raise InvalidTokenError("Invalid token type")
        return payload
    except (InvalidTokenError, JWTError):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token",
            headers={"WWW-Authenticate": "Bearer"},
        )
