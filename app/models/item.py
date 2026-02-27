from sqlalchemy import Column, Integer, String, Float, DateTime, Boolean, ForeignKey
from datetime import datetime, timezone
from sqlalchemy.orm import relationship
from app.db.base import Base

class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True) # title
    description = Column(String, nullable=True)
    price = Column(Float)
    # cost = Column(Float)
    quantity = Column(Integer)
    # stock = Column(Integer, default=0)
    category = Column(String)
    # tags = Column(list)
    # status = Column(String, default="active")
    image_url = Column(String, nullable=True)
    # owner_id = Column(Integer)

    # created_at = Column(DateTime, default=datetime.utcnow)
    # updated_at = Column(DateTime, default=datetime.utcnow)
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
    is_active = Column(Boolean, default=True)

    # Relationship
    # owner = relationship("User", back_populates="items")

# Add relationship to User model
# User.items = relationship("Item", back_populates="owner")
