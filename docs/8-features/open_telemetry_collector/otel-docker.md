#

## JAEGER

```bash
docker run -d --name jaeger \

# → Enables OTLP receiver (important!)
  -e COLLECTOR_OTLP_ENABLED=true \

# binding errors
# -e COLLECTOR_OTLP_GRPC_HOST_PORT=0.0.0.0:4317

# → Jaeger Web UI
  -p 16686:16686 \

# → OTLP/gRPC (preferred for Python)
  -p 4317:4317 \

# → OTLP/HTTP (alternative if needed)
  -p 4318:4318 \

  jaegertracing/all-in-one:latest

docker run -d --name jaeger \
  -e COLLECTOR_OTLP_ENABLED=true \
  -p 16686:16686 \
  -p 4317:4317 \
  -p 4318:4318 \
  jaegertracing/all-in-one:latest

#
http://localhost:16686/

```

---

## ZIPKIN

```bash
docker run --rm -d -p 9411:9411 --name zipkin openzipkin/zipkin

#
http://localhost:9411/zipkin/
```

---

##

## docker run -p 4317:4317 -p 4318:4318 otel/opentelemetry-collector
