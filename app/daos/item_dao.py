from sqlalchemy.orm import Session
from app.models.item import Item
from app.schemas.item import (
    ItemCreate, 
    ItemUpdate, 
    ItemResponse, 
    ItemFormBase, 
    ItemFormCreate, 
    ItemFormUpdate, 
    ItemFormResponse
)
from typing import List

from sqlalchemy import and_, func

class ItemDAO:
    """
    Data Access Object (DAO) pattern - SQLAlchemy specific operations

    Responsibility
        👉 ONLY database operations.

        ✅ DAO methods should only handle persistence (add, flush, refresh).
        ✅ They should not commit — leave commit/rollback to the service layer.
    """

    @staticmethod
    def create(db: Session, item_data: ItemFormCreate) -> Item:
        item = Item(**item_data)
        db.add(item)

        db.flush() # Get ID if needed

        # db.commit()
        # db.refresh(item)

        return item

    @staticmethod
    def get_by_id(db: Session, item_id: int) -> Item | None:
        return db.query(Item).filter(Item.id == item_id).first()
    
    @staticmethod
    def get_by_name(db: Session, name: str) -> Item | None:
        return db.query(Item).filter(Item.name == name).first()

    @staticmethod
    def list(db: Session) -> List[Item]:
        return db.query(Item).all()

    @staticmethod
    def update(db: Session, item: Item, update_data: ItemFormUpdate) -> Item | None:
        # db.execute(update(Item).where(Item.id == item_id).values(**update_data))
        for key, value in update_data.items(): # dict(exclude_unset=True).
            setattr(item, key, value)
        db.flush()
        return item
    
    # Soft Delete
    @staticmethod
    def soft_delete(db: Session, item: Item):
        # db.execute(update(Item).where(Item.id == item_id).values(is_active=False))
        item.is_active = False
        db.flush()

    # Hard Delete
    @staticmethod
    def delete(db: Session, item: Item):
        db.delete(item)

    @staticmethod
    def filter(db: Session, filters: dict):
        query = db.query(Item) 
        conditions = [] 
        
        if "category" in filters: 
            conditions.append(Item.category == filters["category"]) 
        if "min_price" in filters: 
            conditions.append(Item.price >= filters["min_price"]) 
        if "max_price" in filters: 
            conditions.append(Item.price <= filters["max_price"]) 
        if conditions: 
            query = query.filter(and_(*conditions)) 
        
        return query.all()

    @staticmethod
    def category_avg_price_stats(db: Session):
        stats = db.query(
            Item.category,
            func.avg(Item.price).label("avg_price")
        ).group_by(Item.category).all()

        return stats

    # Count Items in each category

    # Advanced: Bulk create
    # @staticmethod
    # def bulk_create(db: Session, items_data: List[dict]) -> List[Item]:
    #     items = [Item(**data) for data in items_data]
    #     db.bulk_save_objects(items)
    #     db.flush()
    #     return items