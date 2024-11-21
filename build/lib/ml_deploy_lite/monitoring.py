<<<<<<< HEAD
# ml_deploy_lite/monitoring.py

from prometheus_flask_exporter import PrometheusMetrics

def setup_monitoring(app):
    metrics = PrometheusMetrics(app)
=======
# ml_deploy_lite/monitoring.py

from prometheus_flask_exporter import PrometheusMetrics

def setup_monitoring(app):
    metrics = PrometheusMetrics(app)
>>>>>>> c399d30 (This library  is done on version 0.7  🐍)
    return metrics