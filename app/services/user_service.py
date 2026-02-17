from sqlalchemy.orm import Session

from app.schemas.user import UserCreate, UserUpdate
from app.daos.user_dao import UserDAO
from app.utils.hashing import Hash

class UserService:

    @staticmethod
    def create_user(db: Session, user_data):
        user_data.password = Hash.bcrypt(user_data.password)
        with db.begin():
            return UserDAO.create(db, user_data.dict())

    @staticmethod
    def get_user(db: Session, user_id: int):
        return UserDAO.get(db, user_id)

    @staticmethod
    def list_users(db: Session):
        return UserDAO.list(db)

    @staticmethod
    def update_user(db: Session, user_id: int, updates):
        with db.begin():
            user = UserDAO.get(db, user_id)
            if not user:
                return None
            return UserDAO.update(db, user, updates.dict(exclude_none=True))

    @staticmethod
    def delete_user(db: Session, user_id: int):
        with db.begin():
            user = UserDAO.get(db, user_id)
            if not user:
                return False
            UserDAO.delete(db, user)
            return True
