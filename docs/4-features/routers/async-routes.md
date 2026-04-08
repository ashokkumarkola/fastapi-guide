# Async vs Sync Routes in FastAPI

## 1. FastAPI and Async Basics

- FastAPI is inherently **async-first** — built to work efficiently with **async I/O**.
- But it also supports **sync routes**, which can confuse beginners into thinking async & sync behave the same.

---

## 2. Key DifferenceAsync Routes

FastAPI is an async framework, in the first place. It is designed to work with async I/O operations and that is the reason it is so fast.

However, FastAPI doesn't restrict you to use only async routes, and the developer can use sync routes as well. This might confuse beginner developers into believing that they are the same, but they are not.
I/O Intensive Tasks

Under the hood, FastAPI can effectively handle both async and sync I/O operations.

    FastAPI runs sync routes in the threadpool and blocking I/O operations won't stop the event loop from executing the tasks.
    If the route is defined async then it's called regularly via await and FastAPI trusts you to do only non-blocking I/O operations.

The caveat is that if you violate that trust and execute blocking operations within async routes, the event loop will not be able to run subsequent tasks until the blocking operation completes.

import asyncio
import time

from fastapi import APIRouter

router = APIRouter()

@router.get("/terrible-ping")
async def terrible_ping():
time.sleep(10) # I/O blocking operation for 10 seconds, the whole process will be blocked

    return {"pong": True}

@router.get("/good-ping")
def good_ping():
time.sleep(10) # I/O blocking operation for 10 seconds, but in a separate thread for the whole `good_ping` route

    return {"pong": True}

@router.get("/perfect-ping")
async def perfect_ping():
await asyncio.sleep(10) # non-blocking I/O operation

    return {"pong": True}

What happens when we call:

    GET /terrible-ping
        FastAPI server receives a request and starts handling it
        Server's event loop and all the tasks in the queue will be waiting until time.sleep() is finished
            Server thinks time.sleep() is not an I/O task, so it waits until it is finished
            Server won't accept any new requests while waiting
        Server returns the response.
            After a response, server starts accepting new requests
    GET /good-ping
        FastAPI server receives a request and starts handling it
        FastAPI sends the whole route good_ping to the threadpool, where a worker thread will run the function
        While good_ping is being executed, event loop selects next tasks from the queue and works on them (e.g. accept new request, call db)
            Independently of main thread (i.e. our FastAPI app), worker thread will be waiting for time.sleep to finish.
            Sync operation blocks only the side thread, not the main one.
        When good_ping finishes its work, server returns a response to the client
    GET /perfect-ping
        FastAPI server receives a request and starts handling it
        FastAPI awaits asyncio.sleep(10)
        Event loop selects next tasks from the queue and works on them (e.g. accept new request, call db)
        When asyncio.sleep(10) is done, servers finishes the execution of the route and returns a response to the client

Warning

Notes on the thread pool:

    Threads require more resources than coroutines, so they are not as cheap as async I/O operations.
    Thread pool has a limited number of threads, i.e. you might run out of threads and your app will become slow. Read more (external link)

### **Async routes (`async def`)**

- Executed within the **event loop**.
- Expected to contain **non-blocking I/O** only.
- If you insert blocking operations inside an async route → the **event loop is blocked** → entire server becomes unresponsive.

### **Sync routes (`def`)**

- FastAPI runs them inside a **threadpool executor**.
- Blocking I/O inside sync routes **does not block the event loop**.
- Only blocks a single worker thread.

---

## 3. How FastAPI Handles I/O

| Route Type                            | Execution              | Blocking Effect        |
| ------------------------------------- | ---------------------- | ---------------------- |
| **Async route with non-blocking I/O** | Runs inside event loop | Not blocking           |
| **Async route with blocking I/O**     | Blocks event loop      | Entire server pauses   |
| **Sync route with blocking I/O**      | Runs in threadpool     | Blocks only one thread |

---

## 4. Code Example

```python
import asyncio
import time
from fastapi import APIRouter

router = APIRouter()

@router.get("/terrible-ping")
async def terrible_ping():
    time.sleep(10)  # ❌ Blocking inside async route
    return {"pong": True}

@router.get("/good-ping")
def good_ping():
    time.sleep(10)  # ✔ Blocking allowed (runs in threadpool)
    return {"pong": True}

@router.get("/perfect-ping")
async def perfect_ping():
    await asyncio.sleep(10)  # ✔ Non-blocking async call
    return {"pong": True}
```

---

## 5. What Happens Internally?

### **GET /terrible-ping (async + blocking I/O → BAD)**

1. Request arrives.
2. `time.sleep(10)` blocks the **event loop**.

   - Server cannot process **any new requests**.
   - Entire FastAPI app becomes frozen.

3. After 10 seconds, response returns.
4. Event loop resumes accepting requests.

### **GET /good-ping (sync + blocking I/O → OK)**

1. FastAPI receives request.
2. Runs `good_ping()` inside the **threadpool**.
3. Blocking happens on a **worker thread**, not event loop.
4. Event loop continues handling other tasks (DB calls, new requests).
5. Worker thread returns response after sleep finishes.

### **GET /perfect-ping (async + non-blocking I/O → BEST)**

1. `asyncio.sleep(10)` is awaited.
2. Event loop continues processing other tasks during sleep.
3. After await completes, response is sent.

---

## 6. Threadpool Warning ⚠️

- Threads are **heavier** than coroutines.
- Threadpool size is **limited**; too many sync blocking calls can:

  - Exhaust threads
  - Slow down the app
  - Increase latency

Use sync routes wisely when dealing with heavy blocking operations.

---

## 7. Recommended Best Practices

✔ Use **async routes** for:

- Database drivers with async support
- HTTP calls via `httpx.AsyncClient`
- File I/O using aiofiles
- Non-blocking sleeps, delays, queues

✔ Use **sync routes** for:

- CPU-heavy tasks
- Libraries that have no async support (e.g., some ML libs, PDFs, PIL)

❌ Avoid blocking operations (**`time.sleep`, heavy loops**, file operations) inside `async def`.

---
