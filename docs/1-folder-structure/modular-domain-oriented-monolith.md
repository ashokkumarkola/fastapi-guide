# 📦 Modular Domain-Oriented Structure

```bash
app/
│
├── core/                  # Shared infrastructure
│   ├── app.py             # FastAPI app factory
│   ├── config.py          # Settings loader (Pydantic BaseSettings)
│   ├── database.py        # SQLAlchemy session, engine
│   ├── security.py        # Auth, JWT, password hashing
│   ├── logging.py         # Logging config
│   ├── exceptions.py      # Custom exception handlers
│   ├── middlewares.py     # Global middlewares (CORS, logging, error handling)
│   └── lifespan.py        # Startup/shutdown events
│
├── common/                # Shared utilities
│   ├── utils/             # Helper functions
│   ├── enums.py
│   ├── validators.py
│   ├── responses.py
│   ├── helpers.py
│   └── datetime.py
│
├── api/                   # API layer
│   ├── dependencies/      # Request-level dependencies (auth, db session, pagination)
│   │   └── auth.py
│   └── v1/
│       └── router.py      # Central router for v1 (aggregates module routers)
│
├── modules/               # Each domain is self-contained
│   ├── users/
│   │   ├── models.py
│   │   ├── schemas.py
│   │   ├── repository.py
│   │   ├── service.py
│   │   ├── routes.py
│   │   └── constants.py
│   │
│   ├── products/
│   │   ├── models.py
│   │   ├── schemas.py
│   │   ├── repository.py
│   │   ├── service.py
│   │   ├── routes.py
│   │   └── constants.py
│   │
│   ├── orders/
│   │   ├── models.py
│   │   ├── schemas.py
│   │   ├── repository.py
│   │   ├── service.py
│   │   ├── routes.py
│   │   └── constants.py
│   │
│   ├── payments/
│   │   ├── models.py
│   │   ├── schemas.py
│   │   ├── repository.py
│   │   ├── service.py
│   │   ├── routes.py
│   │   └── constants.py
│   │
│   └── reviews/
│       ├── models.py
│       ├── schemas.py
│       ├── repository.py
│       ├── service.py
│       ├── routes.py
│       └── constants.py
│
├── integrations/          # External services
│   ├── redis.py
│   ├── stripe.py
│   ├── razorpay.py
│   ├── email.py
│   └── s3.py
│
├── tasks/                 # Background jobs (Celery, RQ, APScheduler)
│   ├── email_tasks.py
│   ├── order_tasks.py
│   └── notification_tasks.py
│
├── workers/               # Worker entrypoints (Celery/RQ workers)
│   └── worker.py
│
├── tests/                 # Organized by domain
│   ├── conftest.py        # Pytest fixtures
│   ├── test_users.py
│   ├── test_products.py
│   ├── test_orders.py
│   ├── test_payments.py
│   └── test_reviews.py
│
├── alembic/               # Migration scripts
│   ├── versions/
│   └── env.py
│
├── alembic.ini            # Alembic config
│
├── main.py                # FastAPI entrypoint
│
│
├── requirements/          # Environment-specific dependencies
│   ├── base.txt
│   ├── dev.txt
│   └── prod.txt
│
├── .env                   # Environment variables (DB_URL, SECRET_KEY, etc.)
├── .env.example           # Example env file for onboarding
├── .gitignore             # Ignore venv, __pycache__, logs, secrets
├── Dockerfile             # Container build
├── docker-compose.yml     # Local dev stack (app + db + redis)
├── pyproject.toml         # Poetry/Black/Isort config (if using Poetry)
├── setup.cfg              # Linting/formatting config (Flake8, Isort)
├── Makefile               # Common dev commands (test, lint, run)
├── README.md              # Project documentation
│
└── CI/                    # CI/CD pipeline configs
    ├── github-actions.yml # GitHub Actions workflow
    └── gitlab-ci.yml      # GitLab CI config (optional)

```

---

## Run this in terminal from your project root:

```bash
mkdir -p app/{core,common/{utils},api/{dependencies,v1},modules/{users,products,orders,payments,reviews},integrations,tasks,workers,tests,alembic/versions,requirements,CI}

touch app/core/{app.py,config.py,database.py,security.py,logging.py,exceptions.py,middlewares.py,lifespan.py}

touch app/common/{enums.py,validators.py,responses.py,helpers.py,datetime.py}

touch app/api/dependencies/auth.py
touch app/api/v1/router.py

touch app/modules/users/{models.py,schemas.py,repository.py,service.py,routes.py,constants.py}

touch app/modules/products/{models.py,schemas.py,repository.py,service.py,routes.py,constants.py}

touch app/modules/orders/{models.py,schemas.py,repository.py,service.py,routes.py,constants.py}

touch app/modules/payments/{models.py,schemas.py,repository.py,service.py,routes.py,constants.py}

touch app/modules/reviews/{models.py,schemas.py,repository.py,service.py,routes.py,constants.py}

touch app/integrations/{redis.py,stripe.py,razorpay.py,email.py,s3.py}

touch app/tasks/{email_tasks.py,order_tasks.py,notification_tasks.py}

touch app/workers/worker.py

touch app/tests/{conftest.py,test_users.py,test_products.py,test_orders.py,test_payments.py,test_reviews.py}

touch app/alembic/env.py

touch alembic.ini
touch main.py

touch app/requirements/{base.txt,dev.txt,prod.txt}

touch .env .env.example .gitignore Dockerfile docker-compose.yml pyproject.toml setup.cfg Makefile README.md

touch app/CI/{github-actions.yml,gitlab-ci.yml}
```

---

## Then create Python packages (**init**.py) everywhere:

```bash
find app -type d -exec touch {}/__init__.py \;
```
