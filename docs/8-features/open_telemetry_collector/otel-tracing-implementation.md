# 1️⃣ Ways to Implement Tracing in FastAPI

There are **3 main approaches**.

| Method                     | Description                                 | When to use        |
| -------------------------- | ------------------------------------------- | ------------------ |
| **Auto Instrumentation**   | Automatically traces frameworks & libraries | Default choice     |
| **Manual Instrumentation** | You create spans in code                    | For custom logic   |
| **Hybrid**                 | Auto + manual spans                         | Most real projects |

---

# 2️⃣ Auto Instrumentation (Recommended Base)

This automatically traces:

- HTTP requests
- FastAPI routes
- DB calls
- outgoing requests

### Install

```bash
pip install \
opentelemetry-api \
opentelemetry-sdk \
opentelemetry-exporter-otlp \
opentelemetry-instrumentation-fastapi \
opentelemetry-instrumentation-asgi
```

---

### Basic Setup

`instrumentation.py`

```python
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter

trace.set_tracer_provider(TracerProvider())

tracer_provider = trace.get_tracer_provider()

otlp_exporter = OTLPSpanExporter(endpoint="http://localhost:4318/v1/traces")

span_processor = BatchSpanProcessor(otlp_exporter)

tracer_provider.add_span_processor(span_processor)
```

---

### Attach to FastAPI

```python
from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor

app = FastAPI()

FastAPIInstrumentor.instrument_app(app)
```

Now each request becomes a **span automatically**.

Example:

```
GET /users/3
```

creates:

```
HTTP span
```

---

# 3️⃣ Manual Instrumentation

Used when you want **custom spans around business logic**.

### Example

```python
from opentelemetry import trace

tracer = trace.get_tracer(__name__)

def get_user(user_id):
    with tracer.start_as_current_span("get_user_logic"):
        return db.fetch_user(user_id)
```

Now the trace becomes:

```
HTTP request
   └── get_user_logic
```

---

# 4️⃣ Span Attributes

Add metadata to spans.

```python
with tracer.start_as_current_span("get_user") as span:
    span.set_attribute("user.id", user_id)
```

Example attributes:

```
user.id = 3
db.system = postgres
```

Used for filtering traces.

---

# 5️⃣ Error Tracking

Capture exceptions.

```python
try:
    risky_operation()
except Exception as e:
    span.record_exception(e)
    span.set_status(Status(StatusCode.ERROR))
```

Now trace shows **error span**.

---

# 6️⃣ Context Propagation

This allows traces to **continue across services**.

Example:

```
API → Auth Service → DB
```

Trace ID travels in headers:

```
traceparent
```

FastAPI instrumentation handles this automatically.

---

# 7️⃣ Exporters (Where traces go)

Common backends:

| Backend        | Purpose            |
| -------------- | ------------------ |
| Jaeger         | tracing UI         |
| Zipkin         | tracing UI         |
| Grafana Tempo  | production tracing |
| OTEL Collector | central pipeline   |

Typical flow:

```
FastAPI
   ↓
OpenTelemetry SDK
   ↓
OTLP Exporter
   ↓
Collector
   ↓
Jaeger / Tempo / Zipkin
```

---

# 8️⃣ Sampling (Important in Production)

Tracing **every request is expensive**.

Use sampling.

Example:

```
10% of requests traced
```

Code:

```python
from opentelemetry.sdk.trace.sampling import TraceIdRatioBased

TracerProvider(
    sampler=TraceIdRatioBased(0.1)
)
```

---

# 9️⃣ Common Instrumentations

Add tracing for dependencies.

Examples:

| Library    | Instrumentation                          |
| ---------- | ---------------------------------------- |
| SQLAlchemy | opentelemetry-instrumentation-sqlalchemy |
| requests   | opentelemetry-instrumentation-requests   |
| redis      | opentelemetry-instrumentation-redis      |

Example:

```python
from opentelemetry.instrumentation.requests import RequestsInstrumentor

RequestsInstrumentor().instrument()
```

---

# 🔟 Best Architecture

Recommended structure:

```
app/
 ├── main.py
 ├── core/
 │     └── instrumentation.py
 ├── api/
 └── services/
```

Startup flow:

```
main.py
   ↓
init telemetry
   ↓
start FastAPI
```

---

# 1️⃣1️⃣ Best Practices

### 1. Use auto instrumentation first

Manual only where needed.

---

### 2. Name spans clearly

Bad:

```
span1
```

Good:

```
fetch_user_from_db
```

---

### 3. Add important attributes

```
user.id
order.id
db.statement
```

---

### 4. Avoid too many spans

Too many spans = performance overhead.

---

### 5. Use batch exporter

Better performance.

```
BatchSpanProcessor
```

---

# Example Final Trace

Request:

```
GET /users/3
```

Trace structure:

```
HTTP GET /users/{id}
   ├── validate_request
   ├── fetch_user_service
   │       └── db.query
   └── format_response
```

Total time breakdown visible.

---

# Final Summary

Tracing implementation usually follows:

```
1 Setup SDK
2 Add FastAPI instrumentation
3 Add manual spans for business logic
4 Send traces to backend
5 Add sampling
```

---
