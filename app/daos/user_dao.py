
from fastapi import HTTPException, status
from sqlalchemy import asc, desc, or_
from sqlalchemy.orm import Session

from app.models.user import User
from app.schemas.user import UserQueryParams


class UserDAO:

    # -------- CREATE -------- #
    @staticmethod
    def create(db: Session, data: dict) -> User:
        """
            User(user_data.model_dump()) # returns a dictionary
            User(**user_data.model_dump()) # Unpacks dict into keyword args
            User.model_validate(user_data) # Direct validation

            # extra keywords
            UserInDB(**user_in.model_dump(), hashed_password=hashed_password)
        """
        # user = User(
        #     email = data.email,
        #     username = data.username,
        #     password = data.password,
        #     fullname = data.fullname
        # )
        user = User(**data)
        db.add(user)
        db.flush()
        return user
    
    # -------- GET -------- #
    @staticmethod
    def get(db: Session, user_id: int) -> User | None:
        return (
            db.query(User)
            .filter(User.id == user_id).first()
        )

    @staticmethod
    def get_by_id(db: Session, user_id: int) -> User | None:
        return (
            db.query(User)
            .filter(User.id == user_id).first()
        )
    
    @staticmethod
    def get_active_by_id(db: Session, user_id: int) -> User | None:
        return ( 
            db.query(User)
            .filter(User.id == user_id, User.is_active == False)
            .first()
        )
    
    @staticmethod
    def get_by_email(db: Session, email: str) -> User | None:
        return (
            db.query(User)
            .filter(User.email == email).first()
        )
    
    # -------- GET LIST -------- #
    @staticmethod
    def list(db: Session):
        return db.query(User).all()
    
    # -------- FULL UPDATE -------- #
    @staticmethod
    def update(db: Session, user: User,  updates: dict) -> User:
        for key, value in updates.items():
            setattr(user, key, value)
        db.flush()
        return user
    
    # -------- PARTIAL UPDATE -------- #
    # @staticmethod
    # def partial_update(db: Session, user: User,  updates: dict) -> User:
    #     for key, value in updates.items():
    #         setattr(user, key, value)
    #     db.flush()
    #     return user
    
    @staticmethod
    def delete(db: Session, user: User):
        db.delete(user)

    @staticmethod
    def bulk_create(db: Session, users_data):
        try:
            # Create User objects from dictionaries
            users = [User(**user_data) for user_data in users_data]
            
            # Add all users to session
            db.add_all(users)
            db.commit()

            # Refresh all objects so IDs are available
            for user in users:
                db.refresh(user)

            return users

        except Exception as e:
            db.rollback()
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Error creating users: {str(e)}"
            )

    @staticmethod
    def verify_unique_email(db: Session, emails):
        return db.query(User.email).filter(User.email.in_(emails)).all()

    @staticmethod
    def filter_users(db: Session, params: UserQueryParams):

        query = db.query(User)

        # ---- filtering ----
        if params.email:
            # query = query.filter(User.email == params.email)
            query = query.filter(User.email.ilike(params.email))

        # ---- search ----
        if params.search:
            search = f"%{params.search}%"
            query = query.filter(
                or_(
                    User.username.ilike(search),
                    User.full_name.ilike(search),
                    User.email.ilike(search),
                )
            )

        # ---- sorting ----
        sort_column = getattr(User, params.sort_by, User.id)

        if params.order.lower() == "desc":
            query = query.order_by(desc(sort_column))
        else:
            query = query.order_by(asc(sort_column))

        # ---- pagination ----
        total = query.count()

        offset = (params.page - 1) * params.size

        users = (
            query.offset(offset)
            .limit(params.size)
            .all()
        )

        return total, users

    # -------- SOFT DELETE -------- #
    @staticmethod
    def soft_delete(db: Session, user: User):
        user.is_active= False 
        # user.is_deleted = True
        # user.deleted_at = datetime.utcnow() 

        db.add(user) 
        db.commit() 
        db.refresh(user) 
        return None

    # -------- HARD DELETE -------- #
    @staticmethod
    def hard_delete(db: Session, user: User):
        db.delete(user)
        db.commit()

    @staticmethod
    def upload_profile_photo(db: Session, user: User):
        db.add(user)
        db.commit()
        db.refresh(user)
        return None
