from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.utils.hashing import Hash
from app.services.user_service import UserService
from app.daos.user_dao import UserDAO

# from app.core.security import verify_password, get_password_hash, create_access_token, create_refresh_token, verify_access_token
from app.core.security_legacy import verify_password, get_password_hash, create_access_token, create_refresh_token, verify_access_token

class AuthService:
    """
        Authentication Service
    """

    @staticmethod
    def register(db: Session, data: dict):
        # data.password = Hash.bcrypt(data.password)

        user = UserService.create_user(db, data)

        access = create_access_token(user.id)
        refresh = create_refresh_token(user.id)

        return (access, refresh)

    @staticmethod
    def login(db: Session, username: str, password: str):
        """
        Process login: authenticate user and generate tokens
        """

        # Get user by email
        user = UserDAO.get_by_email(db, username)

        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, 
                detail="Invalid credentials, User Not Found",
                # headers={"WWW-Authenticate": "Bearer"},
            )

        # Verify password
        if not verify_password(password, user.password):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid credentials, Wrong Password",
                # headers={"WWW-Authenticate": "Bearer"},
            )
        
        # if not user or not verify_password(password, user.password):
        #     # Always verify to avoid timing attacks (even on invalid user)
        #     dummy_hash = get_password_hash("dummy")  # Constant-time
        #     verify_password(password, dummy_hash)
        #     raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")

        # Check if user is active
        # if not user.is_active:
        #     raise HTTPException(
        #         status_code=status.HTTP_400_BAD_REQUEST,
        #         detail="Inactive user"
        #     )

        # Generate tokens
        access_token = create_access_token(user.id)
        refresh_token = create_refresh_token(user.id)
        # access_token = create_access_token(data={"sub": user.id})
        # refresh_token = create_refresh_token(data={"sub": user.id}, refresh=True)

        return (access_token, refresh_token)

    # @staticmethod
    # def refresh(refresh_token: str):

    #     try:
    #         payload = verify_access_token(refresh_token)
    #         user_id = payload.get("sub")
    #     except:
    #         raise HTTPException(status_code=401, detail="Invalid refresh token")

    #     new_access = create_access_token(user_id)

    #     return new_access

    # Logout
    # @staticmethod
    # def logout(db: Session, refresh_token: str):
    #     token = RefreshTokenDAO.get_by_token(db, refresh_token)
    #     token.is_revoked = True
    #     db.commit()
    # @staticmethod
    # def logout(refresh_token: str):  # Optional: Blacklist in prod (e.g., Redis)
    #     # For now, just invalidate client-side
    #     pass  # Enhance: Add to blacklist set
    # @staticmethod
    # def refresh(refresh_token: str, db: Session) -> str:
    #     payload = verify_and_decode_token(refresh_token)  # Reuse verify (adapts to type)
    #     if payload.get("type") != "refresh":
    #         raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid refresh token")
    #     user = get_user(db, payload["sub"])
    #     if not user:
    #         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    #     return create_token(data={"sub": user.id})  # New access


    # @staticmethod
    # def refresh_access_token(
    #     db: Session,
    #     refresh_token: str
    # ) -> TokenResponse:
    #     """
    #     Get new access token using refresh token
    #     """
    #     try:
    #         # Verify refresh token
    #         payload = SecurityUtils.verify_token(refresh_token, expected_type="refresh")
    #         user_id = payload.get("sub")
            
    #         if not user_id:
    #             raise HTTPException(
    #                 status_code=status.HTTP_401_UNAUTHORIZED,
    #                 detail="Invalid refresh token"
    #             )
            
    #         # Get user
    #         user = UserService.get_by_id(db, int(user_id))
    #         if not user or not user.is_active:
    #             raise HTTPException(
    #                 status_code=status.HTTP_401_UNAUTHORIZED,
    #                 detail="User not found or inactive"
    #             )
            
    #         # Generate new access token
    #         access_token = SecurityUtils.create_access_token(
    #             subject=user.id,
    #             email=user.email
    #         )
            
    #         return TokenResponse(
    #             access_token=access_token,
    #             refresh_token=refresh_token,  # Return same refresh token
    #             token_type="bearer"
    #         )
            
    #     except JWTError:
    #         raise HTTPException(
    #             status_code=status.HTTP_401_UNAUTHORIZED,
    #             detail="Invalid refresh token"
    #         )