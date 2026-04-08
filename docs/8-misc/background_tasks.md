# ⚙️ Background Tasks (FastAPI)

## 🔹 What are Background Tasks?

Run tasks **after response is sent**

👉 User gets response fast  
👉 Task runs in background

---

## 🔹 Common Use Cases

- 📧 Send emails
- 📂 File processing
- 🧾 Logging
- 🔔 Notifications

---

## 🔹 Import

```python
from fastapi import FastAPI, BackgroundTasks
```

---

## 🔹 Create Task Function

```python
def write_notification(email: str, message: str = ""):
    with open("log.txt", "w") as f:
        f.write(f"notification for {email}: {message}")
```

---

## 🔹 Add Background Task

```python
app = FastAPI()

@app.post("/send-notification/{email}")
async def send_notification(email: str, background_tasks: BackgroundTasks):
    background_tasks.add_task(write_notification, email, message="some notification")
    return {"message": "Sent in background"}
```

---

## 🔹 How it Works

- Request comes in
- Response returned immediately
- Task runs **after response**

---

## 🔹 Dependency Injection

```python
from typing import Annotated
from fastapi import Depends

async def endpoint(
    email: str,
    background_tasks: BackgroundTasks,
    q: Annotated[str, Depends(get_query)]
):
    ...
```

---

## 🔹 Key Concepts

- ⚡ Non-blocking response
- 🧵 Runs in same process
- 📦 Lightweight tasks
- 🔁 No task queue needed

---

## 🔹 Limitations

- ❌ Not for heavy workloads
- ❌ No parallel workers
- ❌ No retry mechanism
- ❌ Tied to same server process

---

## 🔹 When to Use

✅ Small tasks

- Email sending
- Logging
- Minor processing

❌ Heavy tasks

- ML jobs
- Video processing
- Large data pipelines

---

## 🔹 Alternatives (Advanced)

Use task queues for scaling:

- Celery
- Redis / RabbitMQ

👉 Supports:

- Multi-worker
- Distributed systems
- Retry & scheduling

---

## 🔹 Summary

- Fast response + delayed execution
- Simple & built-in
- Best for lightweight background work

---
