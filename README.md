# B5-EKS-Prac

# Simple Web Application on AWS ECS

This repository contains a simple web application with three containers: Frontend, Backend (using Flask), and Database. The application is deployed on AWS ECS using Fargate.

## Directory Structure

simple-web-app/
├── frontend/
│ ├── Dockerfile
│ ├── index.html
├── backend/
│ ├── Dockerfile
│ ├── app.py
│ ├── requirements.txt
├── database/
│ ├── Dockerfile
│ ├── init.sql
├── kubernetes/
│ ├── frontend-deployment.yaml
│ ├── backend-deployment.yaml
│ ├── database-deployment.yaml



## Getting Started

### Prerequisites

- Docker installed
- AWS CLI configured
- kubectl installed and configured for your EKS cluster

### Building and Pushing Docker Images

1. **Authenticate Docker to your ECR registry**:
    ```sh
    aws ecr get-login-password --region <your-region> | docker login --username AWS --password-stdin <aws_account_id>.dkr.ecr.<your-region>.amazonaws.com
    ```

2. **Build and Push Images**:

    - **Frontend**:
      ```sh
      cd frontend
      docker build -t frontend .
      docker tag frontend:latest <aws_account_id>.dkr.ecr.<your-region>.amazonaws.com/frontend:latest
      docker push <aws_account_id>.dkr.ecr.<your-region>.amazonaws.com/frontend:latest
      ```

    - **Backend**:
      ```sh
      cd ../backend
      docker build -t backend .
      docker tag backend:latest <aws_account_id>.dkr.ecr.<your-region>.amazonaws.com/backend:latest
      docker push <aws_account_id>.dkr.ecr.<your-region>.amazonaws.com/backend:latest
      ```

    - **Database**:
      ```sh
      cd ../database
      docker build -t database .
      docker tag database:latest <aws_account_id>.dkr.ecr.<your-region>.amazonaws.com/database:latest
      docker push <aws_account_id>.dkr.ecr.<your-region>.amazonaws.com/database:latest
      ```

### Deploying to ECS

1. **Create an ECS Cluster**:
    - Open the Amazon ECS Console.
    - Click **Create Cluster**.
    - Select **Networking only** (for Fargate) and click **Next step**.
    - Enter a name for your cluster and click **Create**.

2. **Create Task Definitions**:
    - Open the Amazon ECS Console.
    - Click **Task Definitions** in the left navigation pane.
    - Click **Create new Task Definition**.
    - Select **Fargate** and click **Next step**.
    - Enter a name for your task definition.
    - Add container definitions for `frontend`, `backend`, and `database` using the image URIs from ECR.
    - Specify task size and create the task definition.

3. **Create Services**:
    - Open the Amazon ECS Console.
    - Click **Clusters** in the left navigation pane.
    - Select your cluster.
    - Click **Create** in the **Services** tab.
    - Select `Fargate`, choose your task definition, and configure the service settings.
    - Configure network settings and security groups.
    - Enable load balancing for the frontend service.
    - Review and create the service.

### Accessing the Application

1. **Get the Load Balancer DNS Name**:
    - Go to the EC2 Console.
    - Click **Load Balancers** under **Load Balancing**.
    - Find your load balancer and copy the **DNS name**.

2. **Open the DNS Name in your Browser**:
    - Open the DNS name in your browser to see the simple web application.

## Kubernetes Deployment (Optional)

If you prefer deploying your application on EKS, use the provided Kubernetes YAML files.

1. **Apply Kubernetes Configurations**:
    ```sh
    kubectl apply -f kubernetes/frontend-deployment.yaml
    kubectl apply -f kubernetes/backend-deployment.yaml
    kubectl apply -f kubernetes/database-deployment.yaml
    ```

2. **Get the Public IP of the Frontend Service**:
    ```sh
    kubectl get svc frontend-service
    ```

3. **Open the IP in your Browser**:
    - Copy the `EXTERNAL-IP` from the output and open it in your browser to see the simple web application.
