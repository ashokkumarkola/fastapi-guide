from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.schemas.user import UserCreate, UserUpdate, UserPartialUpdate
from app.daos.user_dao import UserDAO
from app.utils.hashing import Hash

class UserService:

    # -------- CREATE -------- #
    @staticmethod
    def create_user(db: Session, user_data):
        user_data.password = Hash.bcrypt(user_data.password)
        with db.begin():
            return UserDAO.create(db, user_data.dict())

    # -------- GET BY ID -------- #
    @staticmethod
    def get_user(db: Session, user_id: int):
        return UserDAO.get(db, user_id)

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
            
            updates = payload.model_dump()
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

    @staticmethod
    def filter_users(db: Session, params):
        total, users = UserDAO.filter_users(db, params)

        return {
            "total": total,
            "page": params.page,
            "size": params.size,
            "users": users,
        }
    
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
