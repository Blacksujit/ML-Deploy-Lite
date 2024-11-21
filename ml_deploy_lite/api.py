from flask import Flask, request, jsonify
import joblib
from prometheus_flask_exporter import PrometheusMetrics
import logging

class MLDeployLite:
    def __init__(self, model_path):
        self.model = joblib.load(model_path)
        self.app = Flask(__name__)
        self.metrics = PrometheusMetrics(self.app)
        self.setup_logging()
        self.setup_routes()

    def setup_logging(self):
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)

    def setup_routes(self):
        @self.app.route('/predict', methods=['POST'])
        def predict():
            data = request.json
            self.logger.info(f"Received data: {data}")
            prediction = self.model.predict([data['features']])
            self.logger.info(f"Prediction: {prediction.tolist()}")
            return jsonify({'prediction': prediction.tolist()})

    def run(self, host='0.0.0.0', port=5000):
        self.app.run(host=host, port=port)

# Example usage:
# if __name__ == '__main__':
#     deployer = MLDeployLite('ml_deploy_lite/model/sample_model.pkl')
#     deployer.run()
