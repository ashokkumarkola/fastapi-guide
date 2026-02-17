## Imports

```py
from datetime import datetime
from decimal import Decimal
from uuid import uuid4

from sqlalchemy import (
    String, Integer, Boolean, DateTime,
    Numeric, Index, CheckConstraint
)
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
```

---

## Declarative Base

### Why Base = declarative_base()

- Python models ↔ SQLAlchemy ORM metadata

```py
#
Base = declarative_base()

# SQLAlchemy 2.0 model
class Base(DeclarativeBase):
    pass
```

---

## Static typing vs Runtime typing

- Static typing
  Errors caught early (compile/dev time)
  Better IDE autocomplete & refactors
  Safer for large/long-term projects
  Slightly more verbose

- Runtime (dynamic) typing
  Faster to write, very flexible
  Errors appear only when code executes
  Risky in large codebases

### What Column does (old style)

    Runtime ORM mapping only
    No real type info for Python
    IDE & mypy guess types ❌
    Allowed but legacy in SQLAlchemy 2.0

```py
name = Column(String(100), nullable=False)
```

### What Mapped + mapped_column adds (2.0 way)

    Explicit Python ↔ DB type contract
    Type safety (mypy/pyright)
    Better autocompletion
    Clear nullable vs non-null
    Future-proof (official recommendation)

```py
name: Mapped[str] = mapped_column(String(100), nullable=False)
```

### Nullable clarity example

```py
# Old – ambiguity
description = Column(String)

# New – explicit
description: Mapped[str | None] = mapped_column(String)
```

---

## Model

```py
class Product(Base):
    __tablename__ = "products"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    description: Mapped[str | None] = mapped_column(String(255))
    price: Mapped[Decimal] = mapped_column(Numeric(10, 2), nullable=False)
    quantity: Mapped[int] = mapped_column(Integer, nullable=False)
    category: Mapped[str] = mapped_column(String(50), nullable=False)

    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    deleted_at: Mapped[datetime | None] = mapped_column(DateTime, nullable=True)

    created_at: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.utcnow
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )

    __table_args__ = (
        CheckConstraint("price >= 0", name="ck_price_positive"),
        CheckConstraint("quantity >= 0", name="ck_quantity_positive"),
        Index("idx_product_name", "name"),
        Index("idx_product_category", "category"),
    )

    def __repr__(self) -> str:
        return f"<Product id={self.id} name={self.name}>"
```

## Gotchas & edge cases

❌ Float for money → precision bugs

❌ Missing constraints → invalid data

❌ No indexes → slow reads

❌ No timestamps → audit issues

❌ Boolean without default → null confusion

## Advanced features (when needed)

Soft delete: deleted_at column

Enum category/status

Versioning (version_id_col)

Row-level locking for inventory

Async ORM (AsyncSession)

Multi-tenant tenant_id column

---

## Triubleshoot

### Add type hints (PEP 484)

```py
def total(price: float, qty: int) -> float:
    return price * qty

```

### Enforce static checks (must-do)

```bash
mypy src/
```

### Use typed libraries (ORM, FastAPI)

```py
from sqlalchemy.orm import Mapped, mapped_column

price: Mapped[float] = mapped_column(nullable=False)

#
def create_product(p: ProductCreate) -> Product:
    ...

```

### Versioning (version_id_col)

- Why: Prevent lost updates (optimistic locking).

```py
# Model
from sqlalchemy import Integer

version_id: Mapped[int] = mapped_column(Integer, nullable=False, default=1)

__mapper_args__ = {
    "version_id_col": version_id
}
```

- What happens
  Update with old version → StaleDataError
  Safe for concurrent writes

### Soft Delete (deleted_at)

```py
# Usage
product.deleted_at = datetime.utcnow()  # soft delete
# Query (active only)
session.query(Product).filter(Product.deleted_at.is_(None))
```

### Row-level locking (inventory safety)

- Why: Avoid overselling stock.

```py
# Transaction
from sqlalchemy import select

stmt = (
    select(Product)
    .where(Product.id == product_id)
    .with_for_update()
)

product = session.execute(stmt).scalar_one()

if product.quantity <= 0:
    raise Exception("Out of stock")

product.quantity -= 1
```

✔ Locks row until transaction ends

### Multi-tenancy (tenant_id)

- Why: SaaS isolation, per-organization data.

```py
# Model
tenant_id: Mapped[int] = mapped_column(index=True, nullable=False)

# Query rule
select(Product).where(
    Product.tenant_id == current_tenant_id
)
```

### Fail fast in development, not production

- Type errors → caught before deploy
- Runtime stays flexible

```

```
