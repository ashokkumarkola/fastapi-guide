# Handling Errors

## Use HTTPException

```py
from fastapi import FastAPI, HTTPException

raise HTTPException(status_code=404, detail="Item not found")
```

> detail can be dict, list

## Add custom headers

```py
headers={"X-Error": "There goes my error"}

raise HTTPException(
status_code=404,
detail="Item not found",
headers={"X-Error": "There goes my error"},
)
```

## Install custom exception handlers

```py
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

# from starlette.requests import Request
# from starlette.responses import JSONResponse

class UnicornException(Exception):
    def __init__(self, name: str):
        self.name = name


@app.exception_handler(UnicornException)
async def unicorn_exception_handler(request: Request, exc: UnicornException):
    return JSONResponse(
        status_code=418,
        content={"message": f"Oops! {exc.name} did something. There goes a rainbow..."},

    )
```

## Override the default exception handlers

```py
from fastapi.exceptions import RequestValidationError

@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(request, exc):
    return PlainTextResponse(str(exc.detail), status_code=exc.status_code)

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc: RequestValidationError):
    message = "Validation errors:"
    for error in exc.errors():
        message += f"\nField: {error['loc']}, Error: {error['msg']}"
    return PlainTextResponse(message, status_code=400)
```

---

## Use the RequestValidationError body

- to log the body and debug it, return it to the user

```py
content=jsonable_encoder({"detail": exc.errors(), "body": exc.body})
```

---

## Reuse FastAPI's exception handlers

- use the exception along with the same default exception

```py
from fastapi.exception_handlers import (
    http_exception_handler,
    request_validation_exception_handler,
)
```
