from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
# from opentelemetry.exporter.console import ConsoleSpanExporter  # For stdout output
from opentelemetry.sdk.trace.export import ConsoleSpanExporter
from opentelemetry.sdk.trace.export import SimpleSpanProcessor
# from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor
# from opentelemetry.instrumentation.sqlalchemy import SQLAlchemyInstrumentor
from opentelemetry.sdk.resources import Resource
# from opentelemetry.semconv.resource import ResourceAttributes

from fastapi import FastAPI
from sqlalchemy.engine import Engine

# tracer_url = os.getenv("OTEL_EXPORTER_OTLP_ENDPOINT")

resource = Resource(attributes={
    "service.name": "fastapi-guide-service"
    # ResourceAttributes.SERVICE_NAME: "fastapi-guide-service"
})

# Set up TracerProvider (manages all tracers/spans in the app)
# provider = TracerProvider() # resource=resource
provider = TracerProvider(resource=resource)

# EXPORTER
# exporter = OTLPSpanExporter(endpoint=tracer_url)
# OTLP Exporter → points to local Jaeger (gRPC on 4317)
#    Use "http://localhost:4318" if you prefer HTTP instead of gRPC
otlp_exporter = OTLPSpanExporter(
    endpoint="http://localhost:4317",   # Note: for gRPC it's http://... even though protocol is gRPC
    insecure=True                       # No TLS for local dev
)

# SpanProcessor: Batches spans (groups them for efficiency) and sends to exporter
processor = BatchSpanProcessor(otlp_exporter) # ConsoleSpanExporter() # exporter
provider.add_span_processor(processor)

# Attach provider globally
trace.set_tracer_provider(provider)

# Create FastAPI app
# app = FastAPI(title="OTel FastAPI Demo")

# Instrument the app (auto-creates spans for every request)
# FastAPIInstrumentor.instrument_app(app)

def get_tracer(name: str = __name__):
    return trace.get_tracer(name)

def instrument_app(app: FastAPI):
    FastAPIInstrumentor.instrument_app(app)

# def instrument_engine(engine: Engine):
#     SQLAlchemyInstrumentor().instrument(engine=engine)


