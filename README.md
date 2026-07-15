# 🚀 Cloud-Native CI/CD Platform for a Python Microservice Application

## 📌 Project Overview

This project demonstrates the implementation of a complete Cloud-Native DevOps platform for deploying a Python Flask microservice using modern DevOps tools and best practices.

The application is containerized using Docker, deployed on Kubernetes, provisioned with Terraform, monitored using Prometheus and Grafana, secured with AWS IAM, Secrets Manager, Kubernetes Secrets, S3 Encryption, and automated using Python scripts.

---

# 🎯 Features

- Python Flask Microservice
- Docker Containerization
- Multi-stage Docker Build
- Non-root Docker User
- Docker Compose Support
- Kubernetes Deployment
- Kubernetes Service
- Kubernetes Secrets
- Kubernetes Health Checks
- Ingress Configuration
- Terraform Infrastructure as Code
- AWS VPC
- AWS EC2
- AWS S3 Bucket
- Server Side Encryption (AES256)
- AWS IAM Least Privilege
- AWS Secrets Manager
- CI/CD Ready Architecture
- Prometheus Monitoring
- Grafana Dashboard
- Alertmanager
- Automated Backup Script
- Automated Cleanup Script

---

# 🛠 Technologies Used

| Category | Technologies |
|----------|--------------|
| Programming | Python 3, Flask |
| Containerization | Docker, Docker Compose |
| Orchestration | Kubernetes, Minikube |
| Infrastructure | Terraform |
| Cloud | AWS |
| Storage | Amazon S3 |
| Security | IAM, AWS Secrets Manager, Kubernetes Secrets |
| Monitoring | Prometheus, Grafana |
| Automation | Python |
| Version Control | Git, GitHub |
| Package Manager | Helm |

---

# 🏗 Project Architecture

```
                    GitHub Repository
                            │
                            │
                    GitHub Actions (Optional)
                            │
                            ▼
                     Docker Build Image
                            │
                            ▼
                      Docker Hub Registry
                            │
                            ▼
                   Kubernetes Deployment
                            │
          ┌─────────────────┴─────────────────┐
          │                                   │
      Flask App                         Kubernetes Service
          │                                   │
          └─────────────────┬─────────────────┘
                            ▼
                        Ingress Controller
                            │
                            ▼
                          Users

----------------------------------------------

Terraform
    │
    ├── AWS VPC
    ├── EC2
    ├── Security Groups
    └── S3 Bucket

----------------------------------------------

Monitoring

Prometheus
      │
      ▼
Grafana Dashboards

----------------------------------------------

Security

IAM
Secrets Manager
Kubernetes Secrets
S3 Encryption
Non-root Docker User

----------------------------------------------

Automation

backup.py
cleanup.py
```

---

# 📂 Project Structure

```
Cloud-Native-CICD-Platform/
│
├── app/
│   ├── app.py
│   ├── requirements.txt
│   ├── Dockerfile
│   └── aws_secrets.py
│
├── kubernetes/
│   ├── deployment.yaml
│   ├── service.yaml
│   ├── ingress.yaml
│   └── secret.yaml
│
├── terraform/
│   ├── provider.tf
│   ├── network.tf
│   ├── compute.tf
│   ├── security.tf
│   ├── s3.tf
│   ├── variables.tf
│   └── terraform.tfvars
│
├── backups/
│   ├── backup.py
│   └── cleanup.py
│
├── logs/
│
├── README.md
│
└── .gitignore
```

---

# ✅ Prerequisites

Install the following tools:

- Python 3.x
- Docker Desktop
- Kubernetes
- Minikube
- kubectl
- Helm
- Terraform
- AWS CLI
- Git

---

# ⚙ Installation

Clone the repository

```bash
git clone https://github.com/<your-username>/<repository>.git

cd <repository>
```

Install Python packages

```bash
pip install -r app/requirements.txt
```

---

# 🐳 Docker Commands

Build Docker Image

```bash
docker build -t flask-devops-app .
```

Run Container

```bash
docker run -p 5000:5000 flask-devops-app
```

View Running Containers

```bash
docker ps
```

Stop Container

```bash
docker stop <container_id>
```

---

# ☸ Kubernetes Deployment

Start Minikube

```bash
minikube start
```

Deploy Application

```bash
kubectl apply -f kubernetes/deployment.yaml

kubectl apply -f kubernetes/service.yaml
```

Check Pods

```bash
kubectl get pods
```

Check Services

```bash
kubectl get svc
```

Deploy Ingress

```bash
kubectl apply -f kubernetes/ingress.yaml
```

---

# ☁ Terraform Infrastructure

Initialize Terraform

```bash
terraform init
```

Validate

```bash
terraform validate
```

Plan

```bash
terraform plan
```

Apply

```bash
terraform apply
```

Destroy Infrastructure

```bash
terraform destroy
```

---

# 📊 Monitoring Setup

Install Monitoring Stack

```bash
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts

helm repo update

helm install monitoring prometheus-community/kube-prometheus-stack -n monitoring
```

Port Forward Grafana

```bash
kubectl port-forward svc/monitoring-grafana 3000:80 -n monitoring
```

Open

```
http://localhost:3000
```

Port Forward Prometheus

```bash
kubectl port-forward svc/monitoring-kube-prometheus-prometheus 9090:9090 -n monitoring
```

Open

```
http://localhost:9090
```

---

# 🔐 Security Features

### IAM Least Privilege

Configured IAM policies with minimum required permissions.

### AWS Secrets Manager

Database credentials stored securely.

### Kubernetes Secrets

Application secrets injected securely into pods.

### Docker Non-root User

Container runs as a non-root user.

Verified using:

```bash
kubectl exec -it <pod-name> -- whoami
```

Output

```
appuser
```

### S3 Server-Side Encryption

AES256 encryption enabled on S3 buckets.

### Terraform Sensitive Variables

Sensitive values stored using Terraform variables.

---

# 🤖 Automation Scripts

## backup.py

Features

- Compresses log files
- Uploads backups to Amazon S3
- Deletes local backups older than 7 days

Run

```bash
python backup.py
```

---

## cleanup.py

Features

- Removes unused Docker images
- Deletes temporary files
- Cleans old log files

Run

```bash
python cleanup.py
```

---

# 📈 Monitoring Dashboard

Grafana dashboards include:

- CPU Usage
- Memory Usage
- HTTP Requests
- Requests per Second
- Kubernetes Pods
- Cluster Health

---

# 🚨 Alerts

Configured Grafana alert rules for:

- Application Down
- High CPU Usage
- High Memory Usage

---

# 📷 Screenshots

Add screenshots of:

```
Project Architecture

Docker Containers

Kubernetes Pods

Kubernetes Services

Ingress

Terraform Apply

AWS EC2

AWS S3

AWS Secrets Manager

IAM Policy

Prometheus Targets

Grafana Dashboard

Grafana Alerts

Automation Script Output

Backup Uploaded to S3
```

---

# 🔮 Future Improvements

- GitHub Actions CI/CD Pipeline
- Jenkins Integration
- SonarQube Code Analysis
- Trivy Container Scanning
- ArgoCD GitOps Deployment
- Horizontal Pod Autoscaler (HPA)
- AWS EKS Deployment
- AWS RDS Integration
- HTTPS using Cert-Manager
- Slack & Email Alert Notifications
- Centralized Logging using ELK Stack
- Multi-Environment Deployments (Dev, QA, Prod)

---

# 👩‍💻 Author

**Rucha Dhamune**

Mechanical Engineer | DevOps Engineer

Skills:

- AWS
- Docker
- Kubernetes
- Terraform
- Jenkins
- Python
- Git
- Linux
- Prometheus
- Grafana

---

# 📄 License

This project is created for learning, portfolio, and demonstration purposes.