# Deployment of Django Application Image in AWS ECR on Minikube

## Overview
This project shows how to deploy a containerized django application stored in AWS ECR to a local Minikube Kubernetes cluster.
This project demonstrates a practical workflow for integrating AWS container registry service with a local k8s environment.

## Tech Stack
- Kubernetes (Minikube)
- Kubectl
- AWS CLI
- Amazon Elastic Container Registry (ECR)
- Django RestFramework
- Docker
- Terraform

## Project Structure
```
Application-deploy
├──voters-app
|   ├── config
|   ├── Core
|   ├── Dockerfile
│   ├── manage.py
│   └── requirements.txt
├── Infrastructure
│   ├── backend.tf
│   ├── ecr.tf
│   ├── provider.tf
│   ├── terraform.tfvars
│   └── variables.tf
├── k8s
│   ├── deployment.yml
│   └── service.yml
└── README.md
```

## Setup
Below are the steps followed to set up and successfully deploy this web application:

1. Clone the repository:
```bash
git clone https://github.com/Adeife79/django-app-deployment-on-minikube.git
```

2.  Authenticate into AWS Account:
```bash
aws configure
```

3. In local terminal, change directory to Infrastructure folder:
```bash
cd Infrastructure
```

4. Initialize and apply terraform:
Note: The S3 bucket used for the Terraform state must already exist in AWS before applying Terraform.
```bash 
terraform init
terraform plan
terraform apply -auto-approve
```

5. Change to the API directory to build and push the docker image to Amazon ECR.
```bash
aws ecr get-login-password --region <aws_region> | docker login --username AWS --password-stdin <account_id>.dkr.ecr.<aws_region>.amazonaws.com
docker build -t <image_name>:tag .
docker tag <image_name>:tag <account_id>.dkr.ecr.<aws_region>.amazonaws.com/<image_name>:tag
docker push <account_id>.dkr.ecr.<aws_region>.amazonaws.com/<image_name>:tag
```

6. Navigate to the k8s directory and create Kubernetes secret:
```bash
kubectl create secret docker-registry ecr-secret \
  --docker-server=<account-id>.dkr.ecr.<region>.amazonaws.com \
  --docker-username=AWS \
  --docker-password="$(aws ecr get-login-password --region <region>)"
```

7.  In the k8s directory, create deployment and service
```bash
kubectl apply -f deployment.yml
kubectl apply -f service.yml
```

8. Check the deployment, service, and pods:
Note: Ensure the state of the pods is **Running**
```bash
kubectl get deployments
kubectl get pods
kubectl get svc
```

9. Get the url to access the application:
```bash
minikube service <service_name>
```

## Contributions
Contributions and suggestions are welcome.



