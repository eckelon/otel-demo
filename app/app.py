import os

from flask import Flask
from opentelemetry import trace
from opentelemetry.exporter.jaeger.thrift import JaegerExporter
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor

app = Flask(__name__)

trace.set_tracer_provider(TracerProvider())
tracer = trace.get_tracer(__name__)

jaeger_exporter = JaegerExporter(
    agent_host_name=os.environ.get("JAEGER_AGENT_HOST", "localhost"),
    agent_port=int(os.environ.get("JAEGER_AGENT_PORT", 6831)),
)
span_processor = BatchSpanProcessor(jaeger_exporter)
trace.get_tracer_provider().add_span_processor(span_processor)


@app.route("/")
def hello():
    with tracer.start_as_current_span("hello-span"):
        return "Hello, World!"


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
