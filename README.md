# ☁️ LEO-CLOUD - AI-Powered Execution Engine 🚀

## 📌 Overview
LEO-CLOUD is the **server-side execution engine** for LEO, responsible for **processing AI-generated commands** securely in a **cloud environment**.

## 🏗️ Architecture
- **FastAPI Backend** – Handles API requests.
- **Google Vertex AI** – Generates accurate shell commands.
- **Secure Execution Engine** – Runs commands safely inside containers.
- **PostgreSQL Database** – Stores logs and execution history.

## 📂 Project Structure
```
leo-cloud/
│── server/                # FastAPI backend
│── infra/                 # Infrastructure (Terraform, Kubernetes)
│── requirements.txt       # Backend dependencies
│── README.md              # Documentation
```

## 🚀 Getting Started
### Deploy Backend
```bash
uvicorn server.main:app --host 0.0.0.0 --port 8000
```

### Deploy Infrastructure
```bash
cd infra/terraform
terraform init
terraform apply
```

## 📜 License
MIT License.
