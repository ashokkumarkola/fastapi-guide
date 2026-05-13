Yes — in **OpenTelemetry the main telemetry signals are 3**:

1️⃣ **Traces**
2️⃣ **Metrics**
3️⃣ **Logs**

---

## 1️⃣ Traces

**Purpose:** Track the **path of a request through services**.

Example request flow:

```
User → API → Service → Database
```

Trace contains:

- **Trace** → whole request journey
- **Span** → one operation
- **Span attributes** → metadata (method, URL, DB query)
- **Parent/child relation** → shows call hierarchy
- **Duration** → how long each step took
- **Status** → success / error

Example span:

```
Span: GET /users
Duration: 45ms
Attributes:
  http.method=GET
  http.status_code=200
```

Used for:

- debugging slow requests
- understanding service dependencies

---

## 2️⃣ Metrics

**Purpose:** **Numerical measurements over time**.

Examples:

```
CPU usage
Request count
Memory usage
Error rate
```

Types of metrics:

- **Counter** → always increases
  - `http_requests_total`

- **Gauge** → current value
  - `memory_usage`

- **Histogram** → distribution
  - request latency

Example metric:

```
http_requests_total = 250
request_latency = 120ms
```

Used for:

- dashboards
- alerts
- system health monitoring

---

## 3️⃣ Logs

**Purpose:** **Event records from the application**.

Example log:

```
2026-03-09 INFO User login successful
2026-03-09 ERROR Database connection failed
```

Logs contain:

- **timestamp**
- **severity level** (INFO, WARN, ERROR)
- **message**
- **attributes / context**
- **trace_id (optional)**

Example:

```
level=ERROR
message="DB connection failed"
trace_id=abc123
```

Used for:

- debugging errors
- auditing events
- investigating failures

---

## Relationship between them

```
Logs → event details
Metrics → numbers & trends
Traces → request flow
```

Example debugging case:

```
Metric: error rate increased
Trace: request slow at DB
Logs: "database timeout"
```

Together they give **full observability**.

---

✅ **Summary**

| Signal  | What it shows          |
| ------- | ---------------------- |
| Traces  | Request flow           |
| Metrics | Numerical measurements |
| Logs    | Event messages         |

These **3 are the core signals of OpenTelemetry**.
