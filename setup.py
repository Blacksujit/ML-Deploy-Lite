from setuptools import setup, find_packages

setup(
    name='ml_deploy_lite',
    version='0.7',
    packages=find_packages(),
    install_requires=[
        'Flask',
        'gunicorn',
        'docker',
        'pyyaml',
        'joblib',
        'scikit-learn',
        'prometheus_flask_exporter'
    ],
    description='A library to simplify your ML model deployments',
    long_description='''\

# ML Deploy Lite

The ML Deploy Lite Library is a powerful and user-friendly solution designed to simplify the deployment of machine learning models in production environments. This library provides a comprehensive set of tools and utilities to facilitate the management, serving, and monitoring of machine learning models, making it easier for developers and data scientists to integrate their models into applications.

Installation:
To install the library, run the following command:

```
pip install ml_deploy_lite
```

## Key Features:
- Model Serving: The library offers robust APIs for serving machine learning models, allowing users to expose their models as RESTful services. This enables easy integration with web applications and other services.

- Version Management: ML Deploy Lite supports versioning of machine learning models, enabling users to manage multiple versions of their models seamlessly. This feature is crucial for maintaining and updating models in production without downtime.

- Monitoring and Logging: The library includes built-in monitoring tools to track model performance and usage metrics. Users can log requests, responses, and performance statistics to ensure their models are functioning optimally.

- Containerization Support: ML Deploy Lite provides utilities for containerizing machine learning models using Docker, facilitating easy deployment across various environments, including cloud platforms and on-premises servers.

- Configuration Management: Users can easily configure deployment settings, such as model paths, API endpoints, and logging preferences, through a simple configuration file, allowing for flexible and customizable deployments.

- Integration with Popular Frameworks: The library is designed to work seamlessly with popular machine learning frameworks like TensorFlow, PyTorch, and Scikit-learn, making it a versatile choice for developers.

## Getting Started:

1. Prepare Your Model:
   Ensure you have a trained machine learning model saved in a format compatible with joblib. For example:
   ```python
   import joblib
   from sklearn.datasets import load_iris
   from sklearn.ensemble import RandomForestClassifier

   iris = load_iris()
   X, y = iris.data, iris.target
   model = RandomForestClassifier()
   model.fit(X, y)
   joblib.dump(model, 'model/sample_model.pkl')
   ```

2. Deploy Your Model:
   Use the MLDeployLite class to deploy your model:
   ```python
   from ml_deploy_lite import MLDeployLite

   deployer = MLDeployLite('model/sample_model.pkl')
   deployer.run()
   ```

3. Making Predictions:
   Send a POST request to the /predict endpoint:
   ```bash
   curl -X POST http://localhost:5000/predict -H "Content-Type: application/json" -d '{"features": [5.1, 3.5, 1.4, 0.2]}'
   ```

4. Monitoring and Logging:
   The library automatically logs incoming requests and predictions. You can customize the logging level in the setup_logging method.

5. Docker Integration:
   To create a Docker image for your application, use the provided create_dockerfile function in ml_deploy_lite/docker.py.

6. Kubernetes Integration:
   To create a Kubernetes deployment configuration, use the create_k8s_deployment function in ml_deploy_lite/k8s.py.

## Conclusion:

The ML Deploy Lite Library is designed to make the deployment of machine learning models straightforward and efficient. With its robust features and easy-to-use interface, you can quickly turn your models into production-ready services. For more information, check the GitHub repository for documentation and updates: https://github.com/Blacksujit/ML-Deploy-Lite.git

''',
    long_description_content_type='text/markdown',  # or 'text/plain' if you prefer plain text
    author='Sujit Nirmal (@blacksujit)',
    author_email='nirmalsujit981@gmail.com',
    keywords=[
        "Python",  # Use terms users are likely to search for.
        "Machine Learning",
        "Deep Learning",
        "MLops",
        "Deployements",
        "Model-Deployement",
        "ML-models",
        "state-of-art-deployements",
    ],
    url='https://github.com/Blacksujit/ML-Deploy-Lite.git',
    classifiers=[
        'Intended Audience :: Developers',
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        'Operating System :: OS Independent',
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires='>=3.6',
 
)