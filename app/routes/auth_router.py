from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.models.user import User
from app.schemas.user import UserCreate, UserResponse, Login
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

@router.post("/register", status_code=status.HTTP_201_CREATED)
def register(body: UserCreate, db: Session = Depends(get_db)):
    return AuthService.register_user(db, body)

@router.post('/login') # , response_model=UserResponse
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
 