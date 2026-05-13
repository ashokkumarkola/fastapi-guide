# **Basic SQLAlchemy Column Data Types**

### String & Text Types

```python
from sqlalchemy import (
    String, Text, Unicode, UnicodeText, CLOB,
    CHAR, VARCHAR, NCHAR, NVARCHAR
)
```

- `String(length=None, collation=None, ...)` - Variable length string
- `Text(length=None, collation=None)` - Variable length text
- `CHAR(length=None, collation=None)` - Fixed length character
- `VARCHAR(length=None, collation=None)` - SQL standard VARCHAR
- `Unicode(length=None, collation=None)` - Unicode string (Python 3: same as String)
- `UnicodeText(length=None, collation=None)` - Unicode text (Python 3: same as Text)
- `CLOB(length=None, collation=None)` - Character Large Object
- `NCHAR(length=None, collation=None)` - National char (Unicode)
- `NVARCHAR(length=None, collation=None)` - National varchar (Unicode)

### Numeric Types

```python
from sqlalchemy import (
    Integer, BigInteger, SmallInteger,
    Float, Numeric, Decimal,
    Double, DoublePrecision, REAL
)
```

- `Integer` - 32-bit integer
- `BigInteger` - 64-bit integer
- `SmallInteger` - 16-bit integer
- `Float(precision=None, asdecimal=False, decimal_return_scale=None)` - Floating point
- `Numeric(precision=None, scale=None, asdecimal=True, decimal_return_scale=None)` - Arbitrary precision
- `Decimal(precision=None, scale=None, asdecimal=True, decimal_return_scale=None)` - Same as Numeric
- `Double(precision=None, asdecimal=False, decimal_return_scale=None)` - Double precision (some backends)
- `DoublePrecision(precision=None, asdecimal=False, decimal_return_scale=None)` - SQL standard DOUBLE PRECISION
- `REAL(precision=None, asdecimal=False, decimal_return_scale=None)` - Single precision

### Boolean & Binary Types

```python
from sqlalchemy import (
    Boolean, LargeBinary, BLOB, BYTEA,
    Binary, VARBINARY
)
```

- `Boolean(create_constraint=False, name=None)` - Boolean
- `LargeBinary(length=None)` - Binary data
- `BLOB(length=None)` - Binary Large Object
- `BYTEA()` - PostgreSQL bytea type
- `Binary(length=None)` - SQL standard BINARY
- `VARBINARY(length=None)` - SQL standard VARBINARY

### Date & Time Types

```python
from sqlalchemy import (
    DateTime, Date, Time, TIMESTAMP,
    Interval
)
```

- `DateTime(timezone=False)` - Date and time
- `Date()` - Date only
- `Time(timezone=False)` - Time only
- `TIMESTAMP(timezone=False)` - SQL TIMESTAMP
- `Interval(native=True, second_precision=None, day_precision=None)` - Time interval

### JSON & Special Types

```python
from sqlalchemy import (
    JSON, ARRAY, Enum, PickleType,
    UUID, Uuid
)
```

- `JSON(none_as_null=False)` - JSON data type
- `ARRAY(item_type, as_tuple=False, dimensions=None)` - Array type (PostgreSQL)
- `Enum(*enums, **kw)` - Enumeration type
- `PickleType(protocol=5, pickler=None, comparator=None)` - Python object pickling
- `UUID(as_uuid=True)` - UUID type (some backends)
- `Uuid(as_uuid=True)` - Alternative UUID type

### Other SQL Types

```python
from sqlalchemy import (
    REAL, FLOAT, DOUBLE, NUMERIC, DECIMAL,
    SMALLINT, BIGINT, TINYINT,
    BINARY, VARBINARY, CLOB, NCLOB
)
```

## **Domain-Specific Types**

```python
from sqlalchemy.dialects import postgresql, mysql, sqlite

# PostgreSQL specific
from sqlalchemy.dialects.postgresql import (
    INET, CIDR, MACADDR, MONEY,
    TSVECTOR, JSONB, HSTORE, OID,
    BYTEA, UUID
)

# MySQL specific
from sqlalchemy.dialects.mysql import (
    YEAR, SET, TINYINT, MEDIUMINT,
    LONGTEXT, MEDIUMTEXT, TINYTEXT,
    LONGBLOB, MEDIUMBLOB, TINYBLOB
)
```

## **Constraint & Index Types**

```python
from sqlalchemy import (
    Index, CheckConstraint, UniqueConstraint,
    PrimaryKeyConstraint, ForeignKeyConstraint
)
```

## **Complete Import Example**

```python
from sqlalchemy import (
    # String types
    String, Text, CHAR, VARCHAR, CLOB,

    # Numeric types
    Integer, BigInteger, SmallInteger,
    Float, Numeric, Decimal,

    # Boolean & Binary
    Boolean, LargeBinary, BLOB,

    # Date/Time
    DateTime, Date, Time, TIMESTAMP,

    # Special types
    JSON, ARRAY, Enum, PickleType, UUID,

    # Constraints
    Index, CheckConstraint, UniqueConstraint,
    PrimaryKeyConstraint, ForeignKeyConstraint
)

# PostgreSQL extensions
from sqlalchemy.dialects.postgresql import JSONB, UUID as PG_UUID

# MySQL extensions
from sqlalchemy.dialects.mysql import YEAR, LONGTEXT
```

## **Official Documentation Reference**

According to SQLAlchemy's [official Column and Data Types documentation](https://docs.sqlalchemy.org/en/20/core/type_basics.html):

1. **Generic Types** - Work across all backends
2. **SQL Standard Types** - Map to SQL standard types
3. **Vendor-Specific Types** - In `sqlalchemy.dialects`
4. **Custom Types** - Create your own with `TypeDecorator`

## **Usage Example**

```python
from sqlalchemy import Column
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    email = Column(String(100), unique=True)
    age = Column(Integer)
    salary = Column(Numeric(10, 2))
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime)
    metadata = Column(JSON)  # For JSON data
    avatar = Column(LargeBinary)  # For binary files
```

# **Note**: Some types like `Index` and `CheckConstraint` are **not column datatypes** but **table-level constructs** for creating indexes and constraints.
