# TREE

```bash
tree
tree -L 2

tree -I "venv"

tree -d
tree -a
tree -h
tree -f

tree > structure.txt
```

---

.
├── alembic.ini
├── app
│   ├── all*models.py
│   ├── constants
│   │   ├── constants.py
│   │   └── **init**.py
│   ├── constants.py
│   ├── core
│   │   ├── app.py
│   │   ├── config.py
│   │   ├── **init**.py
│   │   ├── instrumentation.py
│   │   ├── lifespan.py
│   │   ├── logger.py
│   │   ├── middleware.py
│   │   ├── **pycache**
│   │   │   ├── app.cpython-310.pyc
│   │   │   ├── config.cpython-310.pyc
│   │   │   ├── **init**.cpython-310.pyc
│   │   │   ├── instrumentation.cpython-310.pyc
│   │   │   ├── lifespan.cpython-310.pyc
│   │   │   ├── logger.cpython-310.pyc
│   │   │   ├── middleware.cpython-310.pyc
│   │   │   ├── security.cpython-310.pyc
│   │   │   └── security_legacy.cpython-310.pyc
│   │   ├── security_legacy.py
│   │   └── security.py
│   ├── daos
│   │   ├── auth_dao.py
│   │   ├── blog_dao.py
│   │   ├── **init**.py
│   │   ├── item_dao.py
│   │   ├── **pycache**
│   │   │   ├── blog_dao.cpython-310.pyc
│   │   │   ├── **init**.cpython-310.pyc
│   │   │   ├── item_dao.cpython-310.pyc
│   │   │   └── user_dao.cpython-310.pyc
│   │   └── user_dao.py
│   ├── database.py
│   ├── db
│   │   ├── base.py
│   │   ├── dependencies.py
│   │   ├── **init**.py
│   │   ├── items_data.py
│   │   ├── **pycache**
│   │   │   ├── base.cpython-310.pyc
│   │   │   ├── **init**.cpython-310.pyc
│   │   │   └── session.cpython-310.pyc
│   │   └── session.py
│   ├── dependencies
│   │   ├── auth.py
│   │   ├── **init**.py
│   │   └── **pycache**
│   │   ├── auth.cpython-310.pyc
│   │   └── **init**.cpython-310.pyc
│   ├── exceptions
│   │   ├── db_exceptions.py
│   │   └── **pycache**
│   │   └── db_exceptions.cpython-310.pyc
│   ├── **init**.py
│   ├── main_app.py
│   ├── main.py
│   ├── middleware
│   │   ├── cors.py
│   │   └── **pycache**
│   │   └── cors.cpython-310.pyc
│   ├── models
│   │   ├── blog.py
│   │   ├── **init**.py
│   │   ├── item.py
│   │   ├── **pycache**
│   │   │   ├── blog.cpython-310.pyc
│   │   │   ├── **init**.cpython-310.pyc
│   │   │   ├── item.cpython-310.pyc
│   │   │   └── user.cpython-310.pyc
│   │   └── user.py
│   ├── otel
│   │   └── tracing.py
│   ├── **pycache**
│   │   ├── all_models.cpython-310.pyc
│   │   ├── database.cpython-310.pyc
│   │   ├── **init**.cpython-310.pyc
│   │   ├── main.cpython-310.pyc
│   │   └── models.cpython-310.pyc
│   ├── repository
│   │   ├── blog_repository.py
│   │   └── **init**.py
│   ├── routes
│   │   ├── auth_router.py
│   │   ├── blog_router.py
│   │   ├── book_router.py
│   │   ├── **init**.py
│   │   ├── item_router.py
│   │   ├── purchase_router.py
│   │   ├── **pycache**
│   │   │   ├── auth_router.cpython-310.pyc
│   │   │   ├── blog_router.cpython-310.pyc
│   │   │   ├── blogs.cpython-310.pyc
│   │   │   ├── books_router.cpython-310.pyc
│   │   │   ├── **init**.cpython-310.pyc
│   │   │   ├── item_router.cpython-310.pyc
│   │   │   ├── purchase_router.cpython-310.pyc
│   │   │   ├── user_router.cpython-310.pyc
│   │   │   └── users.cpython-310.pyc
│   │   └── user_router.py
│   ├── schemas
│   │   ├── blog.py
│   │   ├── book.py
│   │   ├── common.py
│   │   ├── **init**.py
│   │   ├── item.py
│   │   ├── **pycache**
│   │   │   ├── blog.cpython-310.pyc
│   │   │   ├── Blog.cpython-310.pyc
│   │   │   ├── book.cpython-310.pyc
│   │   │   ├── **init**.cpython-310.pyc
│   │   │   ├── item.cpython-310.pyc
│   │   │   ├── token.cpython-310.pyc
│   │   │   ├── user.cpython-310.pyc
│   │   │   └── User.cpython-310.pyc
│   │   ├── token.py
│   │   └── user.py
│   ├── services
│   │   ├── auth_service.py
│   │   ├── blog_service.py
│   │   ├── **init**.py
│   │   ├── item_service.py
│   │   ├── **pycache**
│   │   │   ├── auth_service.cpython-310.pyc
│   │   │   ├── blog_service.cpython-310.pyc
│   │   │   ├── **init**.cpython-310.pyc
│   │   │   ├── item_service.cpython-310.pyc
│   │   │   └── user_service.cpython-310.pyc
│   │   └── user_service.py
│   └── utils
│   ├── exceptions.py
│   ├── file_upload.py
│   ├── hashing.py
│   ├── **init**.py
│   ├── **pycache**
│   │   ├── file_upload.cpython-310.pyc
│   │   ├── hashing.cpython-310.pyc
│   │   ├── **init**.cpython-310.pyc
│   │   ├── oauth2.cpython-310.pyc
│   │   ├── security.cpython-310.pyc
│   │   ├── token.cpython-310.pyc
│   │   ├── upload_profile_photo.cpython-310.pyc
│   │   └── validations.cpython-310.pyc
│   ├── upload_profile_photo.py
│   └── validations.py
├── data
│   ├── items.json
│   └── users.json
├── database
│   ├── blog.db
│   ├── fastapi_guide.db
│   └── fastapi_guide.sqlite
├── DockerFile
├── docs
│   ├── automatic docs
│   │   ├── ReDoc.md
│   │   └── Swagger-Ui.md
│   ├── database
│   │   ├── base.md
│   │   ├── database.md
│   │   ├── db.md
│   │   ├── engine-conn-mngment.md
│   │   ├── setup-config.md
│   │   └── sql-alchemy.md
│   ├── features
│   │   ├── models
│   │   │   ├── datatypes.md
│   │   │   └── models.md
│   │   ├── routers
│   │   │   ├── async-routes.md
│   │   │   ├── parameters
│   │   │   │   ├── body-parameters.md
│   │   │   │   ├── body-parameters-validations.md
│   │   │   │   ├── path-parameters.md
│   │   │   │   ├── path-parameters-validations.md
│   │   │   │   ├── query-parameters.md
│   │   │   │   ├── query-parameters-models.md
│   │   │   │   ├── query-parameters-validations.md
│   │   │   │   └── validations.md
│   │   │   ├── routers.md
│   │   │   └── update.md
│   │   ├── schemas
│   │   │   ├── composite_schemas.md
│   │   │   ├── datatypes.md
│   │   │   └── schemas.md
│   │   └── service
│   │   └── services.md
│   ├── folder-structure
│   │   └── tree.md
│   ├── git.md
│   ├── index.md
│   ├── middlewares
│   │   ├── cors.md
│   │   └── middlewares.md
│   ├── misc
│   │   ├── background_tasks.md
│   │   ├── containerize-dockerize.md
│   │   ├── dependency-injection.md
│   │   ├── migrations.md
│   │   ├── plug-ins.md
│   │   ├── pydantic-validation.md
│   │   ├── server_sent_events.md
│   │   ├── starlette-features.md
│   │   ├── static_files.md
│   │   └── transformation.md
│   ├── open_telemetry_collector
│   │   ├── basics.md
│   │   ├── core-signals.md
│   │   ├── docker.md
│   │   ├── fastapi-setup.md
│   │   ├── node-setup.md
│   │   ├── open-telemetry.md
│   │   ├── otel-docker.md
│   │   ├── otel-trace.md
│   │   └── otel-tracing-implementation.md
│   ├── security-authentication
│   │   ├── api-keys.md
│   │   ├── http.md
│   │   ├── jwt.md
│   │   └── Oauth2.md
│   ├── setup
│   │   ├── install-n-setup.md
│   │   ├── project_structure.md
│   │   ├── requirements.md
│   │   └── start-deploy.md
│   ├── testing
│   │   ├── test_client.md
│   │   └── testing.md
│   ├── theory
│   │   ├── advanced.md
│   │   ├── basic.md
│   │   └── modern-python.md
│   └── utilities
│   └── exceptions.md
├── logs
│   ├── app.log
│   └── purchases.txt
├── migrations
│   ├── env.py
│   ├── **pycache**
│   │   └── env.cpython-310.pyc
│   ├── README
│   ├── script.py.mako
│   └── versions
│   ├── 05c97ed42ccf_added_timstamps_to_item_and_removed*.py
│   ├── 60f40b02b769*initial_schema.py
│   ├── 76d88adfeefd_enhanced_item.py
│   ├── 97a5bb1eed2d_enhanced_user_timestamps.py
│   ├── 9ac86fce9415_users_enhanced.py
│   └── **pycache**
│   ├── 05c97ed42ccf_added_timstamps_to_item_and_removed*.cpython-310.pyc
│   ├── 2604d9003995_enhanced_user.cpython-310.pyc
│   ├── 60f40b02b769_initial_schema.cpython-310.pyc
│   ├── 76d88adfeefd_enhanced_item.cpython-310.pyc
│   ├── 97a5bb1eed2d_enhanced_user_timestamps.cpython-310.pyc
│   └── 9ac86fce9415_users_enhanced.cpython-310.pyc
├── mkdocs.yml
├── requirements.txt
├── static
│   ├── others
│   └── public
│   ├── icons8-rest-api-arcade-favicons
│   │   └── web
│   │   ├── icons8-rest-api-arcade-16.png
│   │   ├── icons8-rest-api-arcade-32.png
│   │   └── icons8-rest-api-arcade-96.png
│   └── icons8-star-filled-arcade-favicons
│   └── web
│   ├── icons8-star-filled-arcade-16.png
│   ├── icons8-star-filled-arcade-32.png
│   └── icons8-star-filled-arcade-96.png
├── tests
│   ├── **init**.py
│   ├── **pycache**
│   │   ├── **init**.cpython-310.pyc
│   │   ├── test.cpython-310.pyc
│   │   └── test_main.cpython-310-pytest-9.0.2.pyc
│   └── test_main.py
├── uploads
│   ├── items
│   │   └── 95a1032e-02c5-42c2-8690-ccbfd234bc22_itachi-uchiha.jpg
│   ├── others
│   └── profile_photos

956 directories, 8046 files
