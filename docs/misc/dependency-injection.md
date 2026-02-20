# DEPENDENCIES

## Dependency Injection

Have shared logic (the same code logic again and again).
Share database connections.
Enforce security, authentication, role requirements, etc.

## dependable

```py
from typing import Annotated

from fastapi import Depends, FastAPI

app = FastAPI()


async def common_parameters(q: str | None = None, skip: int = 0, limit: int = 100):
    return {"q": q, "skip": skip, "limit": limit}


CommonsDep = Annotated[dict, Depends(common_parameters)]

@app.get("/items/")
async def read_items(commons: Annotated[dict, Depends(common_parameters)]):
    return commons


@app.get("/users/")
async def read_users(commons: CommonsDep):
    return commons



class CommonQueryParams:
    def __init__(self, q: str | None = None, skip: int = 0, limit: int = 100):
        self.q = q
        self.skip = skip
        self.limit = limit


@app.get("/items/")
async def read_items(commons=Depends(CommonQueryParams)):
    return reponse

@app.get("/items/")
async def read_items(commons: Annotated[CommonQueryParams, Depends(CommonQueryParams)]):
    return response


@app.get("/items/")
async def read_items(commons: Annotated[CommonQueryParams, Depends()]):
    response = {}
    if commons.q:
        response.update({"q": commons.q})
    items = fake_items_db[commons.skip : commons.skip + commons.limit]
    response.update({"items": items})
    return response

```

    /items/public/
    /items/private/
    /users/{user_id}/activate
    /items/pro/

---

## Sub Dependencies

```py
def query_extractor(q: str | None = None):
    return q


def query_or_cookie_extractor(
    q: Annotated[str, Depends(query_extractor)],
    last_query: Annotated[str | None, Cookie()] = None,
):
    if not q:
        return last_query
    return q

@app.get("/items/")
async def read_query(
    query_or_default: Annotated[str, Depends(query_or_cookie_extractor)],
):
    return {"q_or_cookie": query_or_default}
```

---

## Dependencies in path operation decorators

```py
async def verify_token(x_token: Annotated[str, Header()]):
    if x_token != "fake-super-secret-token":
        raise HTTPException(status_code=400, detail="X-Token header invalid")


async def verify_key(x_key: Annotated[str, Header()]):
    if x_key != "fake-super-secret-key":
        raise HTTPException(status_code=400, detail="X-Key header invalid")
    return x_key


@app.get("/items/", dependencies=[Depends(verify_token), Depends(verify_key)])
async def read_items():
    return [{"item": "Foo"}, {"item": "Bar"}]
```

## Global Dependencies

```py
app = FastAPI(dependencies=[Depends(verify_token), Depends(verify_key)])
```

## Dependencies with yield

```py
async def get_db():
    db = DBSession()
    try:
        yield db
    finally:
        db.close()

```

---

## Sub-dependencies with yield

```py
async def dependency_a():
    dep_a = generate_dep_a()
    try:
        yield dep_a
    except InternalError:
        print("Oops, we didn't raise again, ... 😱")
        raise HTTPException(status_code=400, detail=f"Internal error: {e}")
    finally:
        dep_a.close()


async def dependency_b(dep_a: Annotated[DepA, Depends(dependency_a)]):
    dep_b = generate_dep_b()
    try:
        yield dep_b
    finally:
        dep_b.close(dep_a)
```
