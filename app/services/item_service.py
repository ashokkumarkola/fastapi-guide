from sqlalchemy.orm import Session
from app.daos.item_dao import ItemDAO

class ItemService:
    """Item Service"""

    @ staticmethod
    def create_item(db: Session, item_data):
        with db.begin():
            return ItemDAO.create(db, item_data.dict())
        
    @staticmethod
    def get_item(db: Session, item_id: int):
        return ItemDAO.get(db, item_id)
    
    @staticmethod
    def get_items(db: Session):
        return ItemDAO.list(db)
    
    @staticmethod
    def update_item(db: Session, item_id: int, updates: dict):
        with db.begin():
            item = ItemDAO.get(db, item_id)
            if not item:
                return None
            return ItemDAO.update(db, item, updates.dict(exclude_none=True))
    
    @staticmethod
    def delete_item(db: Session, item_id: int):
        with db.begin():
            item = ItemDAO.get(db, item_id)
            if not item:
                return None
            ItemDAO.delete(db, item)
            return True
        
    @staticmethod
    def get_filter_items(db: Session, category: str | None, min_price: float | None, max_price: float | None): 
        filters = {} 
        
        if category: 
            filters["category"] = category 
        if min_price is not None: 
            filters["min_price"] = min_price 
        if max_price is not None: 
            filters["max_price"] = max_price 
        
        return ItemDAO.filter(db, filters)

    @staticmethod
    def get_item_category_avg_price_stats(db: Session):
        return ItemDAO.category_avg_price_stats(db)
    
