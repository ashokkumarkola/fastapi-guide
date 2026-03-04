from fastapi import HTTPException, status
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.schemas import user
from app.schemas.user import UserCreate, UserUpdate, UserPartialUpdate
from app.daos.user_dao import UserDAO
from app.utils.hashing import Hash
# from app.utils.upload_profile_photo import save_upload_file

from app.exceptions.db_exceptions import handle_email_username_integrity_error

from app.schemas.user import (
    UserResponse,
)

class UserService:
    """
        User Service
    """

    # -------- CREATE -------- #
    @staticmethod
    def create_user(db: Session, user_data):

        # Normalize email
        user_data.email = user_data.email.lower()

        # Pre-check (better UX)
        if UserDAO.get_by_email(db, user_data.email):
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT, 
                detail="Email already exists"
            )

        if UserDAO.get_by_username(db, user_data.username):
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Username already exists"
            )
    
        # Hash password
        user_data.password = Hash.bcrypt(user_data.password)

        try:
            with db.begin():
                return UserDAO.create(db, user_data.model_dump())

        except IntegrityError as e:
            db.rollback()
            handle_email_username_integrity_error(e)

    # -------- GET BY ID -------- #
    @staticmethod
    def get_user_by_id(db: Session, user_id: int) -> UserResponse:
        user =  UserDAO.get_by_id(db, user_id)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, 
                detail=f"User with id {user_id} not found"
            )
        return user
    
    # -------- GET BY EMAIL -------- #
    @staticmethod
    def get_user_by_email(db: Session, email: str) -> UserResponse:
        user = UserDAO.get_by_email(db, email)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, 
                detail=f"User with email {email} not found"
            )
        return user
    
    # -------- GET BY USERNAME -------- #
    @staticmethod
    def get_user_by_username(db: Session, username: str) -> UserResponse:
        user = UserDAO.get_by_username(db, username)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, 
                detail=f"User with username {username} not found"
            )
        return user

    # -------- GET BY FULLNAME -------- #
    @staticmethod
    def get_user_by_full_name(db: Session, full_name: str) -> UserResponse:
        user = UserDAO.get_by_full_name(db, full_name)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, 
                detail=f"User with full name {full_name} not found"
            )
        return user

    # -------- GET LIST -------- #
    @staticmethod
    def list_users(db: Session):
        return UserDAO.list(db)

    # -------- PUT (FULL UPDATE) -------- #
    @staticmethod
    def update_user(db: Session, user_id: int, payload: UserUpdate):
        with db.begin():
            user = UserDAO.get_by_id(db, user_id)
            if not user:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail="User not found",
                )
            
            updates = payload.model_dump()
            updates["password"] = Hash.bcrypt(payload.password)

            return UserDAO.update(db, user, updates) # updates.dict(exclude_none=True)
        
    # -------- PATCH (PARTIAL UPDATE) -------- #
    @staticmethod
    def partial_update_user(db: Session, user_id: int, payload: UserPartialUpdate):
        with db.begin():
            user = UserDAO.get_by_id(db, user_id)
            if not user:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail="User not found",
                )
            
            updates = payload.model_dump(exclude_unset=True) # Removes unset/None fields
            if "password" in updates:
                updates["password"] = Hash.bcrypt(
                    updates["password"]
                )

            return UserDAO.update(db, user, updates)
        
    @staticmethod
    def delete_user(db: Session, user_id: int):
        with db.begin():
            user = UserDAO.get(db, user_id)
            if not user:
                return False
            UserDAO.delete(db, user)
            return True
        
    # -------- SOFT DELETE -------- #
    @staticmethod
    def soft_delete_user(db: Session, user_id: int):

        user = UserDAO.get_active_by_id(db, user_id)

        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="User not found",
            )

        UserDAO.soft_delete(db, user)

        return {"message": "User soft deleted"}
    
    # -------- HARD DELETE -------- #
    @staticmethod
    def hard_delete_user(db: Session, user_id: int):

        user = UserDAO.get_active_by_id(db, user_id)

        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="User not found",
            )

        UserDAO.hard_delete(db, user)

        return {"message": "User permanently deleted"}
    
    # -------- Upload Profile Photo -------- #
    # @staticmethod
    # def upload_profile_photo(db, user_id: int, file):

    #     user = UserDAO.get_by_id(user_id)

    #     if not user:
    #         raise HTTPException(status_code=404, detail="User not found")

    #     photo_url = save_upload_file(
    #         file=file,
    #         folder="profile_photos",
    #         allowed_types=["image/jpeg", "image/png", "image/webp"],
    #     )

    #     user.profile_photo = photo_url
    #     db.commit()
    #     db.refresh(user)

    #     return user

    @staticmethod
    def filter_users(db: Session, params):
        total, users = UserDAO.filter_users(db, params)

        return {
            "total": total,
            "page": params.page,
            "size": params.size,
            "users": users,
        }
    
    @staticmethod
    def bulk_create_users(db: Session, users: list[UserCreate]):

        # Check duplicate emails in DB
        emails = [u.email for u in users]

        existing = UserDAO.verify_unique_email(db, emails)

        if existing:
            raise HTTPException(
                status_code=400,
                detail=f"Emails already exist: {[e[0] for e in existing]}",
            )

        # Convert schema -> ORM model safely
        user_objects = []

        for user in users:
            # user_data = user.dict()
            user_data = user.model_dump()  # ✅ Pydantic v2
            user_data["password"] = Hash.bcrypt(user.password)

            user_objects.append(user_data)
            # user_objects.append(User(**user_data)) # ✅ ORM object

        # delegate persistence
        return UserDAO.bulk_create(db, user_objects)