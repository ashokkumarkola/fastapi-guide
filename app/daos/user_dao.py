
from sqlalchemy.orm import Session

from app.models import User
# from api.schemas.user import User

class UserDAO:

    @staticmethod
    def create(db: Session, data: dict) -> User:
        user = User(**data)
        db.add(user)
        db.flush()
        return user
    
    @staticmethod
    def get(db: Session, user_id: int) -> User | None:
        return db.query(User).filter(User.id == user_id).first()
    
    @staticmethod
    def list(db: Session):
        return db.query(User).all()
    
    @staticmethod
    def update(db: Session, user: User,  updates: dict) -> User:
        for key, value in updates.items():
            setattr(user, key, value)
        db.flush()
        return user
    
    @staticmethod
    def delete(db: Session, user: User):
        db.delete(user)
