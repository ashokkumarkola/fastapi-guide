# layered monolith structure

```bash
app/
│
├── api/
│   ├── dependencies/
│   ├── middlewares/
│   ├── routes/
│   └── router.py
│
├── core/
│   ├── config.py
│   ├── database.py
│   ├── security.py
│   ├── logging.py
│   ├── exceptions.py
│   ├── constants.py
│   └── lifespan.py
│
├── db/
│   ├── base.py
│   ├── session.py
│   └── migrations/
│
├── models/
│   ├── user.py
│   ├── role.py
│   ├── category.py
│   ├── product.py
│   ├── product_variant.py
│   ├── inventory.py
│   ├── cart.py
│   ├── order.py
│   ├── payment.py
│   └── review.py
│
├── schemas/
│   ├── auth.py
│   ├── user.py
│   ├── category.py
│   ├── product.py
│   ├── cart.py
│   ├── order.py
│   └── payment.py
│
├── repositories/
│   ├── base.py
│   ├── user.py
│   ├── category.py
│   ├── product.py
│   ├── cart.py
│   ├── order.py
│   └── payment.py
│
├── services/
│   ├── auth.py
│   ├── user.py
│   ├── category.py
│   ├── product.py
│   ├── inventory.py
│   ├── cart.py
│   ├── order.py
│   ├── payment.py
│   └── notification.py
│
├── integrations/
│   ├── redis.py
│   ├── stripe.py
│   ├── razorpay.py
│   ├── email.py
│   └── s3.py
│
├── tasks/
│   ├── email_tasks.py
│   ├── order_tasks.py
│   └── notification_tasks.py
│
├── utils/
│   ├── pagination.py
│   ├── responses.py
│   ├── enums.py
│   ├── validators.py
│   ├── helpers.py
│   └── datetime.py
│
├── tests/
│   ├── conftest.py
│   ├── test_auth.py
│   ├── test_products.py
│   ├── test_orders.py
│   └── test_payments.py
│
├── main.py
│
├── alembic/
├── alembic.ini
│
├── workers/
├── utils/
│
└── requirements/
    ├── base.txt
    ├── dev.txt
    └── prod.txt
```
