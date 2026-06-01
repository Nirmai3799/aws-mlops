# 🚀 AWS MLOps End-to-End Project

This project demonstrates a complete **MLOps pipeline on AWS**, covering infrastructure setup, containerization, deployment, and CI/CD automation.

---

## 📌 What We Built

An end-to-end workflow:

Local Development → Docker → AWS ECR → EC2 Deployment → CI/CD (GitHub Actions)

---

## 🏗️ Architecture

* **EC2 (ARM64 - Graviton)** for hosting application
* **Docker** for containerization
* **Amazon ECR** for container registry
* **GitHub Actions** for CI/CD pipeline

---

## ⚙️ Setup Steps

### 1. AWS Account Setup

* IAM user with programmatic access
* MFA enabled
* Budget alerts configured

---

### 2. EC2 Setup

* Ubuntu ARM64 instance (Graviton)
* Security Group: Port 80 open
* Docker installed and configured

---

### 3. Dockerization

* Created Dockerfile for application
* Built multi-architecture image (amd64 + arm64)

---

### 4. ECR (Elastic Container Registry)

* Created private repository
* Pushed Docker image to ECR

---

### 5. Deployment

* Pulled image from ECR on EC2

* Ran container:

  ```bash
  docker run -d -p 80:80 <ECR_IMAGE_URI>
  ```

* Accessed application via:

  ```
  http://<EC2-PUBLIC-IP>
  ```

---

### 6. CI/CD with GitHub Actions

* Automatically:

  * Builds Docker image
  * Supports multi-architecture
  * Pushes to ECR on every commit

---

## 🧠 Key Learnings

* Handling ARM64 vs AMD64 architecture issues
* Secure authentication with AWS ECR
* Docker multi-platform builds using Buildx
* Real-world deployment flow on AWS
* CI/CD automation for containerized apps

---

## 🚀 Next Steps

* Add AWS CodePipeline for deployment automation
* Integrate SageMaker for ML training pipelines
* Add Feature Store & Model Registry
* Monitoring & logging

---

## 🛠️ Tech Stack

* AWS (EC2, ECR, IAM)
* Docker
* GitHub Actions
* Python (App Layer)

---

## 👨‍💻 Author

Built as part of hands-on MLOps learning journey.
