# tests/test_api.py

import json
import unittest
from ml_deploy_lite.api import MLDeployLite

class TestMLDeployLite(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.app = MLDeployLite('ml_deploy_lite/model/sample_model.pkl')
        cls.client = cls.app.app.test_client()

    def test_predict(self):
        response = self.client.post('/predict', json={'features': [5.1, 3.5, 1.4, 0.2]})
        self.assertEqual(response.status_code, 200)
        self.assertIn('prediction', json.loads(response.data))

if __name__ == '__main__':
    unittest.main()