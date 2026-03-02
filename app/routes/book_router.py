from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from typing import List
from app.db.session import get_db
from app.schemas.book import BookResponse, BookCreate, BookUpdate, Book

router = APIRouter(
    prefix='/books',
    tags='Books'
)

router.get('/', status_code=status.HTTP_201_CREATED, response_model=BookResponse)
async def create_book(book: Book, db: Session = Depends(get_db)):
    pass

router.get('/{book_id}', status_code=status.HTTP_200_OK, response_model=BookResponse)
async def get_book(book_id: int, db: Session = Depends(get_db)):
    pass

router.get('/', status_code=status.HTTP_200_OK, response_model=List[BookResponse])
async def get_books(db: Session = Depends(get_db)):
    pass

router.patch('/book_id', status_code=status.HTTP_202_ACCEPTED, response_model=BookResponse)
async def update_book(book_id: int, book_updates: BookUpdate, db: Session = Depends(get_db)):
    pass

router.delete('/book_id', status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(book_id: int, db: Session = Depends(get_db)):
    pass

