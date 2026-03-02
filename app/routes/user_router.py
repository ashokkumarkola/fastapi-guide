from fastapi import APIRouter, Query, status, HTTPException, Depends, UploadFile, File
from sqlalchemy.orm import Session
import json

from app.schemas.user import UserCreate, UserUpdate, UserPartialUpdate, UserResponse, BulkUserResponse, UserQueryParams, UserSuccessResponse, UserErrorResponse, UsersPaginated
from app.services.user_service import UserService
from app.db.session import get_db

router = APIRouter(
    prefix='/users', 
    tags=['Users']
)

"""
Router Responsibility
    Accept request
    Validate input (Pydantic)
    Call service
    Return response
"""

# -------- GET ALL USERS -------- #
@router.get("/all/", 
    status_code=status.HTTP_200_OK,
    response_model=list[UserResponse],
)
def get_users(db: Session = Depends(get_db)):
    return UserService.list_users(db)

# -------- FILTER USERS -------- #
@router.get("/all/filter", 
    status_code=status.HTTP_200_OK,
    response_model=UsersPaginated,
)
def list_users(
    # page: int = Query(1, ge=1),
    # size: int = Query(10, ge=1, le=100),
    # search: str | None = None,
    # email: str | None = None,
    # sort_by: str = "id",
    # order: str = "asc",
    params: UserQueryParams = Depends(), # Parse query params into UserQueryParams (otherwise treated as request body)
    db: Session = Depends(get_db),
):
    # params = UserQueryParams(
    #     page=page,
    #     size=size,
    #     search=search,
    #     email=email,
    #     sort_by=sort_by,
    #     order=order,
    # )

    return UserService.filter_users(db, params)

# -------- CREATE -------- #                   
@router.post("/", 
    status_code=status.HTTP_201_CREATED,
    response_model=UserResponse,
)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    return UserService.create_user(db, user)

# -------- GET BY ID -------- #
@router.get("/{user_id}", 
    status_code=status.HTTP_200_OK, 
    response_model=UserResponse,
)
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = UserService.get_user(db, user_id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=f"Blog with id {user_id} not found"
        )
    return user

# -------- GET BY EMAIL -------- #


# -------- FULL UPDATE -------- #
@router.put(
    "/{user_id}",
    response_model=UserResponse,
    status_code=status.HTTP_200_OK,
)
def update_user(
    user_id: int,
    payload: UserUpdate,
    db: Session = Depends(get_db),
):
    """
        * Replace entire resource
        * Payload: all fields required
    """
    return UserService.update_user(db, user_id, payload)

# -------- PARTIAL UPDATE -------- #
@router.patch(
    "/{user_id}",
    response_model=UserResponse,
    status_code=status.HTTP_200_OK,
)
def partial_update_user(
    user_id: int,
    payload: UserPartialUpdate,
    db: Session = Depends(get_db),
):
    """
        * Modify selected fields
        * Payload: optional fields
    """
    return UserService.partial_update_user(db, user_id, payload)

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
