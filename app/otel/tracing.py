# Implement Tracing

from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor

# from opentelemetry.exporter.console import ConsoleSpanExporter  # For stdout output
from opentelemetry.sdk.trace.export import ConsoleSpanExporter
from opentelemetry.sdk.trace.export import SimpleSpanProcessor
# from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter

from opentelemetry.sdk.resources import Resource
# from opentelemetry.semconv.resource import ResourceAttributes

from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor
# from opentelemetry.instrumentation.sqlalchemy import SQLAlchemyInstrumentor

from fastapi import FastAPI
from sqlalchemy.engine import Engine

"""
TRACE:
    HTTP requests
    FastAPI routes
    DB calls
    outgoing requests
"""

# Auto Instrumentation (Automatically traces frameworks & libraries)

resource = Resource(attributes={
    "service.name": "fastapi-guide-service"
})

provider = TracerProvider(resource=resource)

otlp_exporter = OTLPSpanExporter(
    endpoint="http://localhost:4317",
    insecure=True
)

processor = BatchSpanProcessor(otlp_exporter)
provider.add_span_processor(processor)

trace.set_tracer_provider(provider)

def get_tracer(name: str = __name__):
    return trace.get_tracer(name)

def instrument_app(app: FastAPI):
    FastAPIInstrumentor.instrument_app(app)

# Manual Instrumentation (You create spans in code)

from opentelemetry import trace

tracer = trace.get_tracer(__name__)

def get_user(user_id):

    try:
        # Span Attributes
        with tracer.start_as_current_span("get_user_logic") as span:

            # Add metadata to spans.
            span.set_attribute("user.id", user_id)

            return user_id
        
    except Exception as e:
        # Error Tracking
        span.record_exception(e)
        # span.set_status(Status(StatusCode.ERROR))
    
# Hybrid (Auto + manual spans)

