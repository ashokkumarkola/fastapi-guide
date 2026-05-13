# FOLDER STRUCTURE

## Recommended Folder Structure

```text id="28b2nq"
app/
├── api/
│   └── v1/
│       ├── auth.py
│       ├── products.py
│       ├── categories.py
│       ├── carts.py
│       ├── orders.py
│       ├── payments.py
│       └── reviews.py
│
├── core/
│   ├── config.py
│   ├── security.py
│   ├── database.py
│   ├── logging.py
│   └── exceptions.py
│
├── models/
├── schemas/
├── repositories/
├── services/
├── dependencies/
├── middleware/
├── workers/
├── utils/
├── tests/
├── alembic/
└── main.py
```

## Better production version

```
app/
├── api/
│   └── v1/
│       ├── endpoints/
│       └── router.py
```

---
