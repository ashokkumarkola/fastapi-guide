## OpenTelemetry Collector

OpenTelemetry Collector (otel-collector) is a vendor-neutral telemetry pipeline service that collects, processes, and exports observability data.

| Telemetry   | Meaning                          | Example             |
| ----------- | -------------------------------- | ------------------- |
| **Traces**  | request journey across services  | API → Auth → DB     |
| **Metrics** | numeric performance measurements | CPU %, request rate |
| **Logs**    | event records                    | errors, warnings    |

Core pipeline:

```
    Application
        ↓
    Receiver
        ↓
    Processor
        ↓
    Exporter
        ↓
    Observability Backend
```

| Component     | Role                                     |
| ------------- | ---------------------------------------- |
| **Receiver**  | accepts telemetry from apps              |
| **Processor** | transforms / filters data                |
| **Exporter**  | sends data to backend                    |
| **Extension** | auxiliary features (auth, health, pprof) |

Typical backends:
Prometheus
Jaeger
Grafana
Tempo
Datadog
New Relic

---

## Why OpenTelemetry Collector Exists

Problem Without Collector
App → Prometheus
App → Jaeger
App → Datadog
App → Loki

Problems:

complex SDK configuration

vendor lock-in

heavy app overhead

duplicated exporters

---

##

---

##

---

##

---

APIs

SDK

17GB sec

Monolith

client
web server
app server
darabase cms

micro service
client
cdn
services

## Observability

Information

MELT

METRICS
EVENTS
LOGS
TRACES

Open telemetry
Opencensus
Opentracing

## Observability

## Standardize the data

## Analysis Data

---

TRACE LOGGING

DISTRIBUTED TRACING
Corelate

SPAN

letency
errors

Context Propagation
Span Context
trace id
span id
trace flags
trace state

    Corelation context
    customer id
    host name
    region
    application related info..

## TRACES

- end-to-end request flows across services

## METRICS

- counters/gauges for performance

## LOGS

- contextual events

## EVENTS

---
