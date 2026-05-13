## Open Telemetry

```md
- OpenTelemetry (OTel) is a CNCF project providing standardized APIs, SDKs, and tools for collecting traces (end-to-end request flows across services), metrics (counters/gauges for performance), and logs (contextual events).

- Telemetry = remote measurement and reporting of data. - Tele → remote / distance - Metry → measurement
```

**API**

- **What:** Interface developers call in code.
- **Example:**

```js
const tracer = trace.getTracer("service");
const span = tracer.startSpan("db-call");
```

- **Provides:** Functions to create **spans, metrics, logs**.
- **Standardized:** Same API works across languages (Node, Python, Java).

**SDK**

- **What:** Implementation that **collects and processes telemetry data**.
- **Example:**
  NodeSDK automatically captures **HTTP/Express requests** and exports them.
- **Provides:**
  - span processors
  - exporters
  - auto-instrumentation

**Tools**

- **What:** Systems that **store and visualize telemetry**.
- **Examples:**
- **Zipkin / Jaeger** → view traces
- **Prometheus** → metrics
- **Grafana** → dashboards

**Standardized means:**
All services send telemetry in the **same format**, so any backend can read it.

Example flow:

```
App → OpenTelemetry → Zipkin / Jaeger / Grafana
```

---

## Core Components:

API (interfaces),
SDK (implementation),
Exporters (to backends like Jaeger/Prometheus),
Collector (processing pipeline),
Instrumentation (auto/manual code hooks).

---

| Telemetry   | Meaning                          | Example             |
| ----------- | -------------------------------- | ------------------- |
| **Traces**  | request journey across services  | API → Auth → DB     |
| **Metrics** | numeric performance measurements | CPU %, request rate |
| **Logs**    | event records                    | errors, warnings    |

---
