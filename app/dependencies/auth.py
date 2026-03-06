from typing import Annotated
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from jose import JWTError

from app.models.user import User
from app.daos.user_dao import UserDAO
from app.db.session import get_db

# from app.core.security import verify_and_decode_token
from app.core.security_legacy import verify_access_token

# -------- OAuth2 scheme  -------- #
# OAuth2 scheme that extracts token from Authorization header
# tokenUrl is the endpoint where client obtains token (for OpenAPI docs)
# oauth2_scheme = OAuth2PasswordBearer(
#     tokenUrl=f"{settings.API_V1_STR}/auth/login",
#     auto_error=False  # Don't auto-raise, we'll handle it
# )

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")

# -------- Current User Dependency -------- #
async def get_current_user(
    db: Annotated[Session, Depends(get_db)],
    token: Annotated[str | None, Depends(oauth2_scheme)] = None
) -> User:
    """
    Dependency to get current authenticated user
    Can be used in any protected endpoint:
    def protected_endpoint(current_user: User = Depends(get_current_user)):
    """

    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    # Check if token exists
    if not token:
        raise credentials_exception
    
    # Verify token
    try:
        payload = verify_access_token(token, token_type="access")
        user_id: str = payload.get("sub")
        if user_id is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    
    # Get user from database
    user = UserDAO.get_by_id(db, int(user_id))
    if user is None:
        raise credentials_exception
    
    return user
            
    
    
    # return verify_access_token(token) #, credentials_exception)

# -------- Optional User Dependency (No 401 if no token) -------- #
# async def get_current_user(
#     db: Annotated[Session, Depends(get_db)],
#     token: Annotated[str | None, Depends(oauth2_scheme)] = None,
# ) -> User:
#     credentials_exception = HTTPException(
#         status_code=status.HTTP_401_UNAUTHORIZED,
#         detail="Could not validate credentials",
#         headers={"WWW-Authenticate": "Bearer"},
#     )
#     payload = verify_and_decode_token(token)
#     user_id: int = int(payload.get("sub"))
#     if user_id is None:
#         raise credentials_exception
#     user = get_user(db, user_id=user_id)
#     if user is None:
#         raise credentials_exception
#     return user

# -------- Active User Check -------- #
# async def get_current_active_user(current_user: Annotated[User, Depends(get_current_user)]) -> User:
    """
    Extension of get_current_user that also checks if user is active
    """
    # if not current_user.is_active:  # Assume User has is_active
    #     raise HTTPException(
    #         status_code=status.HTTP_400_BAD_REQUEST,
    #         detail="Inactive user"
    #     )
#     return current_user

# -------- Optional User (No 401 if no token) -------- #
# async def get_optional_user(
#     db: Annotated[Session, Depends(get_db)],
#     token: Annotated[Optional[str], Depends(oauth2_scheme)] = None
# ) -> Optional[User]:
#     """
#     Optional authentication - doesn't raise if no token
#     Useful for endpoints that work for both authenticated and unauthenticated users
#     """
#     if not token:
#         return None
    
#     try:
#         payload = SecurityUtils.verify_token(token, expected_type="access")
#         user_id: str = payload.get("sub")
#         if user_id:
#             return UserService.get_by_id(db, int(user_id))
#     except JWTError:
#         pass
    
#     return None