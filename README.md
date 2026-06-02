# 🚀 MLOps Deployment Pipeline (FastAPI + Docker + AWS)

## 📌 Project Overview
This project demonstrates a complete **end-to-end MLOps deployment pipeline** using:

- FastAPI (ML app/API)
- Docker (containerization)
- AWS ECR (image registry)
- AWS EC2 (deployment server)
- AWS CodeBuild (build + deploy via SSH)
- AWS CodePipeline (CI/CD automation)

---

## 🏗️ Architecture

GitHub → CodePipeline → CodeBuild → EC2 (Docker Container)

---

## ⚙️ Tech Stack

- Python 3.10
- FastAPI
- Docker
- AWS EC2
- AWS ECR
- AWS CodeBuild
- AWS CodePipeline

---

## 📂 Project Structure


.
├── app.py
├── requirements.txt
├── Dockerfile
└── buildspec.yml


---

## 🐳 Docker Setup

### Dockerfile

```dockerfile
FROM python:3.10-slim

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
☁️ AWS Setup
1. EC2 Instance
Launched Ubuntu/Amazon Linux EC2
Installed Docker
Opened ports:
22 (SSH)
8000 (App access)
2. ECR Repository
Created repository: mlops-app
Pushed Docker image
3. CodeBuild Setup

Used NO_SOURCE and inline buildspec.

buildspec.yml
version: 0.2

phases:
  build:
    commands:
      - echo "Starting deployment"
      - echo "$EC2_KEY" | base64 -d > key.pem
      - chmod 400 key.pem
      - |
        ssh -o StrictHostKeyChecking=no -i key.pem ec2-user@<EC2_PUBLIC_IP> "
          docker pull <ECR_IMAGE_URI>:latest &&
          docker stop mlops-app || true &&
          docker rm mlops-app || true &&
          docker run -d -p 8000:8000 --name mlops-app <ECR_IMAGE_URI>:latest
        "
🔐 Key Handling (Important)
Private key converted to base64
Stored in CodeBuild environment variable: EC2_KEY
base64 -i mlops-key.pem > key.txt
🔄 CodePipeline Flow
Source: GitHub
Build: CodeBuild
Deploy: SSH to EC2 (via CodeBuild)
🚀 Deployment Flow
Push code to GitHub
CodePipeline triggers automatically
CodeBuild runs:
Connects to EC2 via SSH
Pulls latest Docker image
Stops old container
Runs new container
App becomes live
🌐 Access Application
http://<EC2_PUBLIC_IP>:8000
