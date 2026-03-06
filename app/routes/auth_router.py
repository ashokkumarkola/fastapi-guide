from fastapi import APIRouter, Depends, HTTPException, status, Response, Cookie # Path, Query, Cookie, Header
from sqlalchemy.orm import Session
from typing import Annotated
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from app.models.user import User
from app.schemas.user import UserCreate, UserResponse, Login
from app.schemas.token import Token
from app.db.session import get_db
# from app.utils.hashing import Hash
# from app.utils.token import create_access_token
from app.services.auth_service import AuthService
from app.dependencies.auth import get_current_user, oauth2_scheme

router = APIRouter(
    prefix='/auth',
    tags=['Auth']
)

# @router.get("/items/")
# async def read_items(token: Annotated[str, Depends(oauth2_scheme)]): # access_token: str = Cookie(None)
#     return {"token": token}

# Protected example
# @router.get("/users/me", response_model=UserResponse)
# def read_users_me(current_user: UserResponse = Depends(get_current_user)):
#     return current_user




# -------- REGISTER -------- #
@router.post("/register", status_code=status.HTTP_201_CREATED, response_model=Token)
def register(form_data: UserCreate, db: Session = Depends(get_db)):

    access_token, refresh_token = AuthService.register(db, form_data)

    return Token(access_token=access_token, refresh_token=refresh_token, token_type="bearer")
    # return {
    #     "access_token": access,
    #     "refresh_token": refresh
    # }


# -------- LOGIN -------- #
@router.post("/login", status_code=status.HTTP_200_OK, response_model=Token)
def login(
    response: Response,
    db: Annotated[Session, Depends(get_db)],
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()], # json vs form data | body schema vs depends
):
    """
        form_data:
            username
            password
            scope
            client_id
            client_secret

        reponse:
            access_token
            refresh_token
    """

    # ads_id: Annotated[str | None, Cookie()] = None # ads_id: str | None = Cookie(default=None)
    # user_agent: Annotated[str | None, Header()] = None # user_agent: str | None = Header(default=None) # Header(convert_underscores=False)

    # Authenticate and get tokens
    access_token, refresh_token = AuthService.login(db, form_data.username, form_data.password)

    # ---- Local Storage ----- 
    # Store JWT in localStorage - XSS risk

    # --- Set Cookie ---- 
    # Set HTTP-only cookies (more secure than localStorage)
    # response.set_cookie(
    #     key="access_token",
    #     value=f"Bearer {access_token}",
    #     httponly=True,      # Prevents XSS
    #     secure=True,        # HTTPS only (False for local dev)
    #     samesite="lax",     # CSRF protection
    #     max_age=1800,       # 30 minutes
    #     path="/"            # Available for all routes
    # )
    
    # response.set_cookie(
    #     key="refresh_token",
    #     value=refresh_token,
    #     httponly=True,
    #     secure=True,
    #     samesite="lax",
    #     max_age=604800,     # 7 days
    #     path="/"
    # )

    return Token(access_token=access_token, refresh_token=refresh_token)

# -------- LOGOUT -------- #
# @router.post("/logout")
# def logout(response: Response, refresh_token: str = Depends(oauth2_scheme)):  # Use scheme for token

#     AuthService.logout(refresh_token)


#     response.delete_cookie("access_token", path="/")
#     response.delete_cookie("refresh_token", path="/")

    return {"message": "Successfully logged out"}
    
    # return Token(access_token=access_token, refresh_token=refresh_token, token_type="bearer")
    # return {
    #     "access_token": access,
    #     "refresh_token": refresh
    # }

# -------- REFRESH TOKEN -------- #
# @router.post("/refresh", response_model=Token)
# def refresh(
#     response: Response,
#     db: Annotated[Session, Depends(get_db)],
#     refresh_token: str = None,  # From cookie or add form; for simplicity, assume header/cookie extraction
# ):
    
#     # Try to get refresh token from cookie first
#     if not refresh_token:
#         # In real implementation, you'd extract from request.cookies
#         raise HTTPException(
#             status_code=status.HTTP_401_UNAUTHORIZED,
#             detail="Refresh token missing"
#         )

#     new_access_token = AuthService.refresh(db, refresh_token)

#     # response.set_cookie(key="access_token", value=access_token, httponly=True, secure=True, samesite="lax")
#         # Update cookie
#     response.set_cookie(
#         key="access_token",
#         value=f"Bearer {token_response.access_token}",
#         httponly=True,
#         secure=True,
#         samesite="lax",
#         max_age=1800,
#         path="/"
#     )

#     # return Token(access_token=access_token)
#     return {"access_token": new_access_token}
