# ml_deploy_lite/monitoring.py

from prometheus_flask_exporter import PrometheusMetrics

def setup_monitoring(app):
    metrics = PrometheusMetrics(app)
    return metrics