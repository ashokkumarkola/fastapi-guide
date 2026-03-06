import json

from fastapi import APIRouter, Query, status, HTTPException, Depends, UploadFile, File
from sqlalchemy.orm import Session

from app.schemas.user import (
    UserCreate, 
    UserUpdate, 
    UserPartialUpdate, 
    UserResponse, 
    BulkUserResponse, 
    UserQueryParams, 
    UserSuccessResponse, 
    UserErrorResponse, 
    UsersPaginated,
)    
from app.services.user_service import UserService

from app.db.session import get_db

router = APIRouter(
    prefix='/users', 
    tags=['Users'],
    # dependencies=[Depends(get_current_user)],
)

# -------- GET ALL USERS -------- #
@router.get("/all/", 
    status_code=status.HTTP_200_OK,
    response_model=list[UserResponse],
)
def get_users(db: Session = Depends(get_db)) -> list[UserResponse]:
    return UserService.list_users(db)

# -------- FILTER USERS -------- #
@router.get("/all/filter", 
    status_code=status.HTTP_200_OK,
    response_model=UsersPaginated,
)
def list_users(
    params: UserQueryParams = Depends(), 
    db: Session = Depends(get_db),
):
    return UserService.filter_users(db, params)

# -------- CREATE -------- #                   
@router.post("/", 
    status_code=status.HTTP_201_CREATED,
    response_model=UserResponse,
)
def create_user(user_in: UserCreate, db: Session = Depends(get_db)) -> UserResponse:
    return UserService.create_user(db, user_in)

# -------- GET BY ID -------- #
@router.get("/{user_id}", 
    status_code=status.HTTP_200_OK, 
    response_model=UserResponse,
)
def get_user_by_id(user_id: int, db: Session = Depends(get_db)) -> UserResponse:
    return UserService.get_user_by_id(db, user_id)

# -------- GET BY EMAIL -------- #
@router.get("/email/{email}", 
    status_code=status.HTTP_200_OK, 
    response_model=UserResponse,
)
def get_user_by_email(email: str, db: Session = Depends(get_db)) -> UserResponse:
    return UserService.get_user_by_email(db, email)

# -------- GET BY USERNAME -------- #
@router.get("/username/{username}", 
    status_code=status.HTTP_200_OK, 
    response_model=UserResponse,
)
def get_user_by_username(username: str, db: Session = Depends(get_db)) -> UserResponse:
    return UserService.get_user_by_username(db, username)

# -------- GET BY FULL NAME -------- #
@router.get("/full-name/{full_name}", 
    status_code=status.HTTP_200_OK, 
    response_model=UserResponse,
)
def get_user_by_full_name(full_name: str, db: Session = Depends(get_db)) -> UserResponse:
    return UserService.get_user_by_full_name(db, full_name)

# -------- FULL UPDATE -------- #
@router.put(
    "/{user_id}",
    response_model=UserResponse,
    status_code=status.HTTP_200_OK,
)
def update_user(
    user_id: int,
    updates_in: UserUpdate,
    db: Session = Depends(get_db),
):
    return UserService.update_user(db, user_id, updates_in)

# -------- PARTIAL UPDATE -------- #
@router.patch(
    "/{user_id}",
    response_model=UserResponse,
    status_code=status.HTTP_200_OK,
)
def partial_update_user(
    user_id: int,
    updates_in: UserPartialUpdate,
    db: Session = Depends(get_db),
):
    return UserService.partial_update_user(db, user_id, updates_in)

# -------- SOFT DELETE -------- #
@router.delete(
    "/soft-delete/{user_id}",
    status_code=status.HTTP_200_OK,
)
def delete_user(
    user_id: int,
    # hard: bool = Query(False, description="Hard delete user"),
    db: Session = Depends(get_db),
):
    # if hard:
    #     return UserService.hard_delete_user(db, user_id)

    return UserService.soft_delete_user(db, user_id)

# -------- HARD DELETE -------- #
@router.delete(
    "/hard-delete/{user_id}",
    status_code=status.HTTP_200_OK,
)
def hard_delete_user(
    user_id: int,
    db: Session = Depends(get_db),
):
    return UserService.hard_delete_user(db, user_id)

# -------- UPLOAD PROFILE PHOTO -------- #
# @router.post("/users/{user_id}/upload-photo")
# def upload_profile_photo(
#     user_id: int,
#     file: UploadFile = File(...),
#     db: Session = Depends(get_db),
# ):
#     return UserService.upload_profile_photo(db, user_id, file)

# -------- BULK CREATE BY JSON UPLOAD -------- #
@router.post("/bulk-upload", 
    status_code=status.HTTP_201_CREATED, 
    response_model=BulkUserResponse
)
async def bulk_upload_users(
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
):
    if file.content_type != "application/json":
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Only JSON files allowed",
        )

    data = await file.read()

    try:
        users_json = json.loads(data)
    except json.JSONDecodeError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail="Invalid JSON file",
        )
    
    # if not isinstance(users_json, list):
    #     raise HTTPException(
    #         status_code=status.HTTP_400_BAD_REQUEST,
    #         detail="JSON must be a list of users",
    #     )

    try:
        users = [UserCreate(**u) for u in users_json]
    except Exception as e:
        raise HTTPException(422, f"Validation error: {str(e)}")

    created_users = UserService.bulk_create_users(db, users)

    return {
        "message": "Users created successfully",
        "count": len(created_users),
        "users": created_users,
    }

# -------- -------- #
