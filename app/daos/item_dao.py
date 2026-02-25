from sqlalchemy.orm import Session
from app.models.item import Item
# from app.schemas.item import ItemCreate, ItemUpdate, ItemResponse

from sqlalchemy import and_, func

class ItemDAO:
    """Data Access Object (DAO) pattern - SQLAlchemy specific operations"""

    @staticmethod
    def create(db: Session, data: dict) -> Item:
        item = Item(**data)
        db.add(item)
        db.flush()
        # db.commit()
        # db.refresh(item)
        return item

    @staticmethod
    def get(db: Session, item_id: int) -> Item | None:
        return db.query(Item).filter(Item.id == item_id).first()

    @staticmethod
    def list(db: Session):
        return db.query(Item).all()

    @staticmethod
    def update(db: Session, item: Item, updates: dict) -> Item:
        for key, value in updates.items():
            setattr(item, key, value)
        db.flush()
        return item

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