from sqlalchemy.orm import Session
from app.daos.blog_dao import BlogDAO

class BlogService:

    @staticmethod
    def create_blog(db: Session, blog_data):
        with db.begin():
            return BlogDAO.create(db, blog_data.dict())

    @staticmethod
    def get_blog(db: Session, blog_id: int):
        return BlogDAO.get(db, blog_id)

    @staticmethod
    def list_blogs(db: Session):
        return BlogDAO.list(db)

    @staticmethod
    def update_blog(db: Session, blog_id: int, updates):
        with db.begin():
            blog = BlogDAO.get(db, blog_id)
            if not blog:
                return None
            return BlogDAO.update(db, blog, updates.dict(exclude_none=True))

    @staticmethod
    def delete_blog(db: Session, blog_id: int):
        with db.begin():
            blog = BlogDAO.get(db, blog_id)
            if not blog:
                return False
            BlogDAO.delete(db, blog)
            return True
