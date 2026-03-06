from datetime import datetime, timedelta, timezone
from typing import Dict, Any, Union, Dict, Optional, Annotated
from fastapi import HTTPException, status

import hashlib
import base64
from passlib.context import CryptContext

from jose import jwt, JWTError
# from jwt.exceptions import InvalidTokenError  

from app.core.config import get_settings

settings = get_settings()

# -------- PASSWORD CONTEXTS -------- #

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# -------- Hashing Utilities -------- #
def get_password_hash(password: str) -> str:
    """Hash a password"""
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Verify a plain password against a hashed password"""
    return pwd_context.verify(plain_password, hashed_password)

# -------- Token Utilities -------- #
def create_access_token(
    user_id: int,
    # subject: str,  # Usually user_id or email
    expires_delta: timedelta | None = None,
    # **kwargs
) -> str:
    """
    Create JWT access token with short expiry
    subject is typically the user identifier (stored in 'sub' claim)
    """

    # to_encode = data.copy()

    expire = datetime.now(timezone.utc) + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES) # timedelta(days=7) # Timezone Aware

    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(
            minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
        )

    # to_encode.update({"exp": expire, "type": "access"})
    payload = {
        "sub": str(user_id),
        "exp": expire,
        "type": "access",
        # **kwargs
    }
    
    return jwt.encode(payload, settings.SECRET_KEY, algorithm=settings.ALGORITHM)

def create_refresh_token(
    user_id: int,
    # subject: str,
    # **kwargs
) -> str:
    """
    Create JWT refresh token with longer expiry
    Used to obtain new access tokens without re-authentication
    """

    # to_encode = data.copy()

    expire = datetime.now(timezone.utc) + timedelta(
        days=settings.REFRESH_TOKEN_EXPIRE_DAYS
    )

    # to_encode.update({"exp": expire, "type": "refresh"})
    payload = {
        "sub": str(user_id),
        "exp": expire,
        "type": "refresh",
        # **kwargs
    }
    
    return jwt.encode(payload, settings.SECRET_KEY, algorithm=settings.ALGORITHM)

def verify_access_token(
    token: str,
    token_type: str | None = None,
) -> Dict[str, Any]:
    """
    Verify JWT token and return payload
    Can optionally verify token type (access/refresh)
    Raises JWTError if invalid
    """

    try:
        payload = jwt.decode(
            token, 
            settings.SECRET_KEY, 
            algorithms=[settings.ALGORITHM]
        )
        
        # Verify token type if specified
        if ( 
            token_type and 
            payload.get("type") and 
            payload.get("type") != token_type
        ):
            print(payload.get("type"))
            raise JWTError(f"Invalid token type. Expected {token_type}, got {payload.get('type')}")

            # raise JWTError("Invalid token type")
        
        return payload
    except JWTError as e:
        # Re-raise with more specific message
        raise JWTError(f"Token verification failed: {str(e)}")
    
    # return jwt.decode(token, settings.SECRET_KEY, algorithms=settings.ALGORITHM)
