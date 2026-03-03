from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.utils.hashing import Hash
from app.services.user_service import UserService
from app.utils.security import create_access_token, create_refresh_token, verify_access_token

class AuthService:
    """
        Authentication Service
    """

    @staticmethod
    def register(db: Session, data: dict):
        data.password = Hash.bcrypt(data.password)

        user = UserService.create_user(db, data)

        access = create_access_token(user.id)
        refresh = create_refresh_token(user.id)

        return (access, refresh)

    @staticmethod
    def login(db: Session, data: dict):
        
        user = UserService.get_user_by_email(db, data.email)

        if not user:
            raise HTTPException(status_code=400, detail="Invalid credentials, User Not Found")

        if not Hash.verify(data.password, user.password):
            raise HTTPException(status_code=400, detail="Invalid credentials, Wrong Password")

        access = create_access_token(user.id)
        refresh = create_refresh_token(user.id)

        return (access, refresh)

    @staticmethod
    def refresh(refresh_token: str):

        try:
            payload = verify_access_token(refresh_token)
            user_id = payload.get("sub")
        except:
            raise HTTPException(status_code=401, detail="Invalid refresh token")

        new_access = create_access_token(user_id)

        return new_access

    # Logout
    # @staticmethod
    # def logout(db: Session, refresh_token: str):
    #     token = RefreshTokenDAO.get_by_token(db, refresh_token)
    #     token.is_revoked = True
    #     db.commit()
