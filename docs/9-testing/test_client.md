# TestClient

## To use TestClient, first install httpx in venv

```bash
pip install httpx pytest

# To Run
pytest
```

## Create File

```
test_*.py     ✅
*_test.py     ✅

test_main.py
test_app.py
```

## Import TestClient.

```python
from fastapi.testclient import TestClient

```

---

## Intialize

```python
client = TestClient(app)
```

---

## Create Functions

- function name starts with `test_` - standard pytest conventions
- functions are normal def, not async def.
- calls to the client are also normal calls, not using await.
- to use pytest directly without complications.

```python
def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"msg": "Hello World"}
```

---

## client to pass information

```md
To pass a path or query parameter, add it to the URL itself.
To pass a JSON body, pass a Python object (e.g. a `dict`) to the parameter `json`.
If you need to send Form Data instead of JSON, use the `data` parameter instead.
To pass headers, use a `dict` in the `headers` parameter.
For cookies, a `dict` in the `cookies` parameter.
```
