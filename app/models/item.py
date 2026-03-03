from sqlalchemy import Column, Integer, String, Float, DateTime, Boolean, ForeignKey, Text, func,CheckConstraint
from sqlalchemy.dialects.postgresql import NUMERIC
from datetime import datetime, timezone
from sqlalchemy.orm import relationship
from app.db.base import Base

class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(100), nullable=False, unique=True, index=True) # title
    description = Column(Text, nullable=True)
    price = Column(NUMERIC(10, 2), nullable=False)  # Decimal for precision
    # cost = Column(Float)
    # currency = Column(str)

    quantity = Column(Integer, nullable=False, default=0)
    # stock = Column(Integer, default=0)
    # "in_stock": true,
    # "stock_quantity": 0,

    category = Column(String(50), nullable=True, index=True)
    # tags = Column(list)
    # status = Column(String, default="active")
    image_url = Column(String, nullable=True)
    # owner_id = Column(Integer)

    # created_at = Column(DateTime, default=datetime.utcnow)
    # updated_at = Column(DateTime, default=datetime.utcnow)
    # created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    # updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)
    created_at = Column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc)
    )
    updated_at = Column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
        onupdate=lambda: datetime.now(timezone.utc)
    )

    # owner_id = Column(Integer, ForeignKey("users.id"))
    is_active = Column(Boolean, nullable=False, default=True)

    # Relationship
    # owner = relationship("User", back_populates="items")

    __table_args__ = (
        CheckConstraint('price > 0', name='check_price_positive'),
        CheckConstraint('quantity >= 0', name='check_quantity_non_negative'),
    )

# Add relationship to User model
# User.items = relationship("Item", back_populates="owner")
