# ml_deploy_lite/docker.py

def create_dockerfile():
    dockerfile_content = """
    FROM python:3.11-slim

    WORKDIR /app

    COPY requirements.txt .
    RUN pip install --no-cache-dir -r requirements.txt

    COPY . .

    EXPOSE 5000

    CMD ["gunicorn", "-b", "0.0.0.0:5000", "ml_deploy_lite.api:MLDeployLite.run"]
    """
    with open('Dockerfile', 'w') as f:
        f.write(dockerfile_content)