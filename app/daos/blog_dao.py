from sqlalchemy.orm import Session
from ..models import Blog # ORM Model

class BlogDAO:
    """Data Access Object (DAO) pattern - SQLAlchemy specific operations"""
    
    @staticmethod
    def create(db: Session, data: dict) -> Blog:
        blog = Blog(**data)
        db.add(blog)
        db.flush()
        return blog

    @staticmethod
    def get(db: Session, blog_id: int) -> Blog | None:
        return db.query(Blog).filter(Blog.id == blog_id).first()

    @staticmethod
    def list(db: Session):
        return db.query(Blog).all()

    @staticmethod
    def update(db: Session, blog: Blog, updates: dict) -> Blog:
        for key, value in updates.items():
            setattr(blog, key, value)
        db.flush()
        return blog

    @staticmethod
    def delete(db: Session, blog: Blog):
        db.delete(blog)


# class BlogDAO:
#     def __init__(self, db: Session):
#         self.db = db

#     def get(self, blog_id: int) -> Blog | None:
#         return self.db.query(Blog).filter(Blog.id == blog_id).first()

#     def list(self):
#         return self.db.query(Blog).all()
    
#     def create(self, data: dict) -> Blog:
#         blog = Blog(**data)
#         self.db.add(blog)
#         self.db.flush()
#         return blog

#     def update(self, blog: Blog, updates: dict) -> Blog:
#         for key, value in updates.items():
#             setattr(blog, key, value)
#         self.db.flush()
#         return blog

#     def delete(self, blog: Blog):
#         self.db.delete(blog)
