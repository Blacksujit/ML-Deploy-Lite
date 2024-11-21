# ml-deploy-lite

`ml-deploy-lite` is a Python library designed to simplify the deployment of machine learning models. It allows developers to quickly turn their models into REST APIs or gRPC services with minimal configuration. The library integrates seamlessly with Docker and Kubernetes, providing built-in monitoring and logging for performance and error tracking.

## Features

- **Easy Deployment**: Quickly convert machine learning models into REST APIs.
- **Docker Integration**: Automatically generate a Dockerfile for containerization.
- **Kubernetes Support**: Generate Kubernetes deployment configurations easily.
- **Monitoring and Logging**: Built-in support for monitoring performance and logging errors.
- **User-Friendly**: Designed to be easy to use for developers of all skill levels.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Creating a Sample Model](#creating-a-sample-model)
- [Docker Integration](#docker-integration)
- [Kubernetes Integration](#kubernetes-integration)
- [Testing](#testing)
- [Contributing](#contributing)
- [License](#license)

## Installation

To install `ml-deploy-lite`, you can use pip. Make sure you have Python 3.6 or higher installed.


```
pip install ml-deploy-lite

```

## Usage

Here’s a simple example of how to use `ml-deploy-lite` to deploy a machine learning model.

1. **Import the Library**:

```python
from ml_deploy_lite import MLDeployLite
```

2. **Create an Instance**:

```python
deployer = MLDeployLite('path/to/your/model.pkl')
```

3. **Run the API**:

```python
deployer.run()
```

4. **Make Predictions**:

You can make predictions by sending a POST request to the `/predict` endpoint with the following JSON body:

```json
{
    "features": [5.1, 3.5, 1.4, 0.2]
}
```

## Creating a Sample Model

To create a sample machine learning model, you can use the following script:

```python
import joblib
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier

# Load dataset
iris = load_iris()
X, y = iris.data, iris.target

# Train a model
model = RandomForestClassifier()
model.fit(X, y)

# Save the model
joblib.dump(model, 'ml_deploy_lite/model/sample_model.pkl')
```

Run this script to generate a sample model that you can use with `ml-deploy-lite`.

## Docker Integration

To create a Docker image for your application, you can use the provided `create_dockerfile` function in `ml_deploy_lite/docker.py`. This will generate a `Dockerfile` in the root directory of your project.

1. **Generate the Dockerfile**:

```python
from ml_deploy_lite.docker import create_dockerfile

create_dockerfile()
```

2. **Build the Docker Image**:

Run the following command in the terminal:

```bash
docker build -t your_docker_image:latest .
```

3. **Run the Docker Container**:

After building the image, you can run the container with:

```bash
docker run -p 5000:5000 your_docker_image:latest
```

## Kubernetes Integration

To create a Kubernetes deployment configuration, you can use the `create_k8s_deployment` function in `ml_deploy_lite/k8s.py`. This will generate a `k8s_deployment.yaml` file that you can apply to your Kubernetes cluster.

1. **Generate the Kubernetes Deployment File**:

```python
from ml_deploy_lite.k8s import create_k8s_deployment

create_k8s_deployment()
```

2. **Apply the Configuration**:

Run the following command to deploy to your Kubernetes cluster:

```bash
kubectl apply -f k8s_deployment.yaml
```

## Testing

To run the tests for the API, you can use the following command:

```bash
python -m unittest discover -s tests
```

Make sure you have the necessary test data and models in place before running the tests.

## Contributing

Contributions are welcome! If you have suggestions for improvements or new features, please open an issue or submit a pull request.

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit them (`git commit -m 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

For more information, please refer to the [documentation](https://flask.palletsprojects.com/) for Flask and the [Docker SDK for Python](https://docker-py.readthedocs.io/en/stable/).

---


# Conclusion

This `README.md` file provides a comprehensive overview of your `ml-deploy-lite` library, including installation instructions, usage examples, and details on Docker and Kubernetes integration. It is structured to help users understand how to use the library effectively without encountering errors. Feel free to modify any sections to better fit your project's specifics or to add any additional information you think is necessary!

