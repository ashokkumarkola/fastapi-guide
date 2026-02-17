from fastapi import APIRouter, status, HTTPException, Depends
from sqlalchemy.orm import Session

from app.schemas.user import UserCreate, UserResponse
from app.services.user_service import UserService
from app.db.session import get_db

router = APIRouter(prefix='/users', tags=['Users'])
                       
@router.post("/", status_code=status.HTTP_201_CREATED, response_model=UserResponse)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    return UserService.create_user(db, user)

@router.get("/{user_id}", status_code=status.HTTP_200_OK, response_model=UserResponse)
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = UserService.get_user(db, user_id)
    if not user:
        # raise HTTPException(404, "user not found")
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=f"Blog with id {user_id} not found"
        )
    return user
