# Tracing in OpenTelemetry

### Goal

Track **how a request flows through a system** and **how long each step takes**.

Example request:

```id="w5g6ue"
User → API → Service → Database
```

OpenTelemetry records this as a **Trace**.

---

# 1️⃣ Trace

A **trace = entire request lifecycle**.

Example:

```id="fs0v4y"
Trace: GET /users/3
```

A trace contains **multiple spans**.

---

# 2️⃣ Span

A **span = one unit of work**.

Example operations:

```id="xx0hdg"
Span 1 → HTTP request
Span 2 → business logic
Span 3 → database query
```

Structure:

```id="uac1aa"
Trace
 ├── Span (API request)
 │     ├── Span (service logic)
 │     └── Span (database query)
```

Each span records:

- start time
- end time
- operation name
- attributes
- status

---

# 3️⃣ Span Context

Every span carries a **context**.

Contains:

```id="32pm8g"
trace_id
span_id
parent_span_id
```

Example:

```id="v2hgc0"
trace_id: 4bf92f3577b34da6a3ce929d0e0e4736
span_id: 00f067aa0ba902b7
parent_span_id: 3d4f7a8c1e2f
```

This allows **linking spans across services**.

---

# 4️⃣ Attributes

Attributes = **metadata about the span**.

Example:

```id="w2s4pr"
http.method = GET
http.route = /users/{id}
http.status_code = 200
db.system = postgres
```

Used for:

- filtering
- analysis
- debugging

---

# 5️⃣ Events

Events = **important moments inside a span**.

Example:

```id="itdyox"
"cache_miss"
"retry_attempt"
"exception_thrown"
```

Example structure:

```id="75dxn2"
Event:
  name: "db_retry"
  timestamp: 10:32:11
```

---

# 6️⃣ Status

Span can indicate **success or failure**.

Example:

```id="p0q5ij"
status = OK
status = ERROR
```

Error example:

```id="b5ocg6"
status=ERROR
exception.message="Database timeout"
```

---

# 7️⃣ Span Relationships

Types:

### Parent → Child

```id="93ywzb"
API span
   └── DB span
```

### Links (async systems)

```id="tutk92"
Service A span
        ↘
        Service B span
```

Used in **queues / messaging systems**.

---

# 8️⃣ Exporting the Trace

After spans are created:

```id="d5n47d"
App → OTEL SDK → Exporter → Backend
```

Example exporters:

- Zipkin
- Jaeger
- Grafana Tempo
- OTLP collector

---

# Example (FastAPI request)

Request:

```id="p42y21"
GET /users/3
```

Trace:

```id="9kkkzq"
Trace
 ├── HTTP GET /users/3
 │      duration: 40ms
 │
 ├── validate_user
 │      duration: 5ms
 │
 └── DB query
        duration: 30ms
```

In UI you see **where time is spent**.

---

# Why Traces Are Powerful

They help answer:

- Why is the request slow?
- Which service failed?
- Which database query is slow?
- Where did the request break?

---

# Simple Mental Model

```id="h38xal"
Trace = full story
Span = one step
Attributes = details about the step
Events = moments inside the step
```

---
