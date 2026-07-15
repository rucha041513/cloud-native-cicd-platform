from flask import Flask, jsonify
import logging
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST

app = Flask(__name__)

# Logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s"
)

# Metrics
REQUEST_COUNT = Counter(
    "http_requests_total",
    "Total HTTP Requests",
    ["method", "endpoint"]
)

# Home
@app.route("/")
def home():
    REQUEST_COUNT.labels(method="GET", endpoint="/").inc()
    logging.info("Home endpoint accessed")

    return jsonify({
        "message": "Hello from Kubernetes"
    })


# Health Check
@app.route("/health")
def health():
    REQUEST_COUNT.labels(method="GET", endpoint="/health").inc()
    logging.info("Health endpoint accessed")

    return jsonify({
        "status": "Healthy"
    })


# Sample API
@app.route("/api/users")
def users():
    REQUEST_COUNT.labels(method="GET", endpoint="/api/users").inc()
    logging.info("Users endpoint accessed")

    return jsonify([
        {
            "id": 1,
            "name": "Alice"
        },
        {
            "id": 2,
            "name": "Bob"
        }
    ])


# Prometheus Metrics
@app.route("/metrics")
def metrics():
    return generate_latest(), 200, {
        "Content-Type": CONTENT_TYPE_LATEST
    }


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)