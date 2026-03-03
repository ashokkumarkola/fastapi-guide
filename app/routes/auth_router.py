from fastapi import APIRouter, Depends, HTTPException, status, Response, Cookie # Path, Query, Cookie, Header
from sqlalchemy.orm import Session

from app.models.user import User
from app.schemas.user import UserCreate, UserResponse, Login
from app.schemas.token import Token
from app.db.session import get_db
from app.utils.hashing import Hash
from app.utils.token import create_access_token
from fastapi.security import OAuth2PasswordRequestForm

from app.services.auth_service import AuthService

router = APIRouter(
    prefix='/auth',
    tags=['Auth']
)

# @app.get('/')
# def get_auth(db: Session, Depends=get_db)

# REGISTER
@router.post("/register", status_code=status.HTTP_201_CREATED, response_model=Token)
def register(data: UserCreate, db: Session = Depends(get_db)):

    access, refresh = AuthService.register(db, data)

    return {
        "access_token": access,
        "refresh_token": refresh
    }

# LOGIN
@router.post("/login", status_code=status.HTTP_200_OK, response_model=Token)
def login(data: Login, response: Response, db: Session = Depends(get_db)): 
    # ads_id: Annotated[str | None, Cookie()] = None # ads_id: str | None = Cookie(default=None)
    # user_agent: Annotated[str | None, Header()] = None # user_agent: str | None = Header(default=None) # Header(convert_underscores=False)

    access, refresh = AuthService.login(db, data)

    # ---- Local Storage ----- #
    # Store JWT in localStorage - XSS risk

    # --- Set Cookie ---- #
    response.set_cookie(
        key="access_token",
        value=access,
        httponly=True, # JS cannot access cookie - Protects against XSS
        secure=True, # Cookie sent only over HTTPS - Production MUST
        samesite="lax" # Prevents CSRF attacks [strict | lax | None]
    )

    response.set_cookie(
        key="refresh_token",
        value=refresh,
        httponly=True,
        secure=True,
        samesite="lax"
    ) 

    return {
        "access_token": access,
        "refresh_token": refresh
    }

# REFRESH
@router.post("/refresh")
def refresh(token: str):
    new_access = AuthService.refresh(token)
    return {"access_token": new_access}

@router.post("/logout")
def logout(response: Response):
    response.delete_cookie("access_token")
    response.delete_cookie("refresh_token")
    return {"message": "User Logged out Successfully"}

# @router.post("/me")
# def get_current_user(access_token: str = Cookie(None)):
#     payload = decode_token(access_token)
    
# 
@router.post('/loginOAuth') # , response_model=UserResponse
def login(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == request.username).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Invalid Credentials"
        )
        # raise HTTPException(
        #     status_code=status.HTTP_401_UNAUTHORIZED,
        #     detail="Incorrect username or password",
        #     headers={"WWW-Authenticate": "Bearer"},
        # )
    print(f"\n\nUSER: {user}")
    if not Hash.verify(request.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Incorrect password"
        )
    print('VERIFIED\n\n')
    # Gen JWT
    # access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    # access_token = create_access_token(
    #     data={"sub": user.username}, expires_delta=access_token_expires
    # )

    access_token = create_access_token(data={"sub": user.email})

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }
 