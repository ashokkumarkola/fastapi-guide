from fastapi import FastAPI, APIRouter, Depends, Response, status, HTTPException
from sqlalchemy.orm import Session

from app.schemas.blog import BlogCreate, BlogUpdate, BlogResponse
from app.schemas.user import UserBase
from app.services.blog_service import BlogService
from app.db.session import get_db
# from app.utils.oauth2 import get_current_user
from typing import List

router = APIRouter(prefix="/blogs", tags=["Blogs"])

# Create Blog
@router.post("/", status_code=status.HTTP_201_CREATED, response_model=BlogResponse)
def create_blog(blog: BlogCreate, db: Session = Depends(get_db)):
    return BlogService.create_blog(db, blog)

# Get Blog by ID
@router.get("/{blog_id}", status_code=status.HTTP_200_OK, response_model=BlogResponse)
def get_blog(blog_id: int, db: Session = Depends(get_db)):
    blog = BlogService.get_blog(db, blog_id)
    if not blog:
        # raise HTTPException(404, "Blog not found")
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=f"Blog with id {blog_id} not found"
        )
    return blog

# List Blogs
@router.get("/", status_code=status.HTTP_200_OK, response_model=List[BlogResponse])
def get_blogs(
    db: Session = Depends(get_db), 
    # current_user: User = Depends(get_current_user)
):
    return BlogService.list_blogs(db)

# Update Blog
@router.put("/{blog_id}", status_code=status.HTTP_202_ACCEPTED, response_model=BlogResponse)
def update_blog(
    blog_id: int, 
    updates: BlogUpdate, 
    db: Session = Depends(get_db), 
    # current_user: User = Depends(get_current_user)
):
    blog = BlogService.update_blog(db, blog_id, updates)
    if not blog:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=f"Blog with id {id} not found"
        )
    return blog

# Delete Blog
@router.delete("/{blog_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_blog(blog_id: int, db: Session = Depends(get_db)):
    if not BlogService.delete_blog(db, blog_id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=f"Blog with id {blog_id} not found"
        )
    return {"message": "Deleted"}
