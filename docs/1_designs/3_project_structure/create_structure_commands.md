# CREATE FOLDER STRUCTURE

## production version

```bash
mkdir -p app/api/v1/endpoints
mkdir -p app/core
mkdir -p app/models
mkdir -p app/schemas
mkdir -p app/repositories
mkdir -p app/services
mkdir -p app/dependencies
mkdir -p app/middleware
mkdir -p app/workers
mkdir -p app/utils
mkdir -p app/tests
mkdir -p alembic

touch app/main.py

touch app/api/v1/router.py

touch app/api/v1/endpoints/auth.py
touch app/api/v1/endpoints/products.py
touch app/api/v1/endpoints/categories.py
touch app/api/v1/endpoints/carts.py
touch app/api/v1/endpoints/orders.py
touch app/api/v1/endpoints/payments.py
touch app/api/v1/endpoints/reviews.py

touch app/core/config.py
touch app/core/security.py
touch app/core/database.py
touch app/core/logging.py
touch app/core/exceptions.py
```

## Also create **init**.py files.

```bash
touch app/__init__.py
touch app/api/__init__.py
touch app/api/v1/__init__.py
touch app/api/v1/endpoints/__init__.py
touch app/core/__init__.py
touch app/models/__init__.py
touch app/schemas/__init__.py
touch app/repositories/__init__.py
touch app/services/__init__.py
touch app/dependencies/__init__.py
touch app/middleware/__init__.py
touch app/workers/__init__.py
touch app/utils/__init__.py
touch app/tests/__init__.py
```
