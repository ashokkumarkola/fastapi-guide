## Project Setup

```
mkdir otel-fastapi-demo
cd otel-fastapi-demo
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

```

## Install

```bash
pip install fastapi uvicorn

pip install \
opentelemetry-api \
opentelemetry-sdk \
opentelemetry-exporter-console \

opentelemetry-exporter-otlp \
opentelemetry-exporter-otlp-proto-grpc \
opentelemetry-exporter-otlp-proto-http \

opentelemetry-instrumentation-fastapi \
```

What these are:
`opentelemetry-api/sdk:` Core for creating/processing telemetry (API is abstract; SDK implements it).
`opentelemetry-exporter-console:` Dumps data to stdout for dev testing (real-world: swap for OTLP to Jaeger/Zipkin).
`opentelemetry-instrumentation-fastapi:` Auto-hooks into FastAPI's request/response cycle (official contrib lib).

---

##

---

## Run and See Results

```bash
uvicorn app:app --host 0.0.0.0 --port 8000 --reload
```

---
