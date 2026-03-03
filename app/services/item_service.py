from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from app.daos.item_dao import ItemDAO
from app.core.logger import logger

class ItemService:
    """
    Item Service

    Responsibility
        👉 Business logic and rules
        - Validate input (e.g., check for duplicates)
        - Call DAO methods to persist data
        - Handle commit/rollback once per request
        - primary place for meaningful logs because it reflects business outcomes
    
    Transaction Management
        ✅ Context manager style: with db.begin(): ... → no explicit commit needed
        ✅ Manual style: db.add(...), db.commit(), db.refresh(...).

        # item_data = item_data.dict() # Pydantic v1
        # item_data = item_data.model_dump() # Pydantic v2
        # item_data = item_data.model_dump(mode="json")
    """

    @ staticmethod
    def create_item(db: Session, item_data):
        # ❌ Creates two sessions
        # if ItemDAO.get_by_name(db, item_data.name):
        #     raise HTTPException(status_code=409, detail="Item name already exists")
        
        # with db.begin(): # 
            # ❌ “check-then-insert” pattern has a race condition.
            # if ItemDAO.get_by_name(db, item_data.name):
            #     raise HTTPException(status_code=409, detail="Item name already exists")
        
            # item_data = item_data.model_dump(mode="json") # mode="json"

            # item = ItemDAO.create(db, item_data)
            # db.commit() # ❌ commits/rolls back when the block exits

            # logger.info(f"Item created: ID={item.id}")
            # return item
        
        # with db.begin():
        #     return ItemDAO.create(db, item_data)

        try:
            with db.begin():
                # Transformation
                item_data = item_data.model_dump(mode="json")
                
                # Call DAO to create item
                item = ItemDAO.create(db, item_data)
                logger.info(f"Item created: ID={item.id}")

                return item 
            
        except IntegrityError:
            raise HTTPException(status_code=409, detail="Item name already exists")
        
    @staticmethod
    def get_item(db: Session, item_id: int):
        return ItemDAO.get_by_id(db, item_id)
    
    @staticmethod
    def get_items(db: Session):
        return ItemDAO.list(db)
    
    @staticmethod
    def update_item(db: Session, item_id: int, updates: dict):
        with db.begin():
            item = ItemDAO.get_by_id(db, item_id)
            if not item:
                return None
            logger.info(f"Item updated: ID={item_id}")
            return ItemDAO.update(db, item, updates.dict(exclude_none=True))
    
    @staticmethod
    def delete_item(db: Session, item_id: int):
        item = ItemDAO.get_by_id(db, item_id)
        if not item:
            raise HTTPException(status_code=404, detail="Item not found")
        with db.begin():
            ItemDAO.soft_delete(db, item_id)
            db.commit()
            logger.info(f"Item soft-deleted: ID={item_id}")
            return {"message": "Item deactivated successfully"}
        
        # with db.begin():
        #     item = ItemDAO.get_by_id(db, item_id)
        #     if not item:
        #         return None
        #     ItemDAO.delete(db, item)
        #     return True
        
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
    
