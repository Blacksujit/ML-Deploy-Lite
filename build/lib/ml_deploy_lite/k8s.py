# ml_deploy_lite/k8s.py

def create_k8s_deployment():
    """
    This function creates a Kubernetes deployment for the ml-deploy-lite application.
    It writes the deployment configuration to a file named 'k8s_deployment.yaml'.
    """
    k8s_deployment_content = """
    apiVersion: apps/v1
    kind: Deployment
    metadata:
      name: ml-deploy-lite
    spec:
      replicas: 1
      selector:
        matchLabels:
          app: ml-deploy-lite
      template:
        metadata:
          labels:
            app: ml-deploy-lite
        spec:
          containers:
          - name: ml-deploy-lite
            image: your_docker_image:latest
            ports:
            - containerPort: 5000
    """
    with open('k8s_deployment.yaml', 'w') as f:
        f.write(k8s_deployment_content)