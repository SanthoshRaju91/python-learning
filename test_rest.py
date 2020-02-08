from flask import Flask, jsonify, request, render_template
from prometheus_client import Counter, Histogram, REGISTRY, PROCESS_COLLECTOR, PLATFORM_COLLECTOR, GC_COLLECTOR
import requests
import time
import prometheus_client


app = Flask(__name__)

REGISTRY.unregister(PROCESS_COLLECTOR)
REGISTRY.unregister(PLATFORM_COLLECTOR)
REGISTRY.unregister(GC_COLLECTOR)

REQUEST_METRICS = Counter(
    "rfis_master_http_requests",
    "Application requests, responses metrics",
    ["app_name", "method", "path", "status_code"]
)

REQUEST_LATENCY = Histogram(
    "rfis_master_http_requests_latency",
    "Application request latency",
    ["app_name", "method", "path"]
)

def record_requests_metrics(app_name, method, path, status_code):
    REQUEST_METRICS.labels(app_name, method, path, status_code).inc()

def record_requests_latency(app_name, method, path, resp_time):
    REQUEST_LATENCY.labels(app_name, method, path).observe(resp_time)

def start_timer():
    request.start_timer = time.time()

def stop_timer(response):
    resp_time = time.time() - request.start_timer
    record_requests_latency("fraud_search", request.method, request.path, resp_time)
    return response

def capture_request_metrics(response):
    record_requests_metrics("fraud_search", request.method, request.path, response.status_code)
    return response

@app.route("/api/hourly_update", methods=["POST"])
def perform_hourly_update():
    return jsonify({ "status": "success" })

@app.route("/", methods=["GET"])
def index():
    return "Hello"

@app.route("/check", methods=["GET"])
def check_status():
    print("Performing hourly update and checking response")
    res = requests.post("http://0.0.0.0:5000/{}".format("api/hourly_update"), data=None).json()    
    print(res['status'])
    return "Check console."

@app.route("/metrics", methods=["GET"])
def get_metrics():
    return prometheus_client.generate_latest()

@app.route("/fraud_search/admin", methods=["GET"])
def error_out():
    value = 100.0
    percent_memory = value / 0
    return render_template("errored.html", percent_memory=percent_memory)

if __name__ == "__main__":
    app.before_request(start_timer)
    app.after_request(capture_request_metrics)
    app.after_request(stop_timer)
    app.run(host="0.0.0.0", port="5000", debug=False, use_reloader=False)
