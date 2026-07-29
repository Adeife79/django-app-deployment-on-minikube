# Deployment of Django Application from AWS ECR to Minikube

## Overview
This project shows how to deploy a containerized django application stored in AWS ECR to a local Minikube Kubernetes cluster.
This project demonstartes a practical workflow for integrating AWS container registry service with a local k8s environment.

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
├──API
|   ├── API
|   ├── Core
|   ├── db.sqlite3
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

## Local Set Up
Below are the steps followed to set up and successfully deploy this web application:
1. Create a project folder on visual studio code and change to the folder:
```bash
mkdir  <folder_name>
cd <folder_name>
```

2. Clone Django RestFramework application
```bash
git clone 
```

3. Install application requirements.txt
```bash
```

4. Change directory to the cloned application folder and create Dockerfile:
```bash
cd API
touch Dockerfile
```

5. Build docker image and run the application:
```bash
docker build -t <image_name>:tag .
docker run -d --name <container_name> -p 8090:8090 <image_name>
```

6. In the project directory, create terraform folder and files for the required AWS resources:
```bash
mkdir Infrastructure
cd Infrastructure
touch backend.tf ecr.tf provider.tf variables.tf terraform.tfvars
```

7. Authenticate into AWS account:
```bash
aws configure
```

8. Provision AWS resources:
```bash
terraform init
terraform apply -auto-approve
```

9. Login to AWS ECR locally on terminal and push docker image to it:
```bash
aws ecr get-login-password --region <aws_region> | docker login --username AWS --password-stdin <account_id>.dkr.ecr.<aws_region>.amazonaws.com
docker build -t <image_name>:tag .
docker tag <image_name>:tag <account_id>.dkr.ecr.<aws_region>.amazonaws.com/<image_name>:tag
docker push <account_id>.dkr.ecr.<aws_region>.amazonaws.com/<image_name>:tag
```

10. Create k8s folder in the project folder and create `deployment, service, and secret` files:
```bash
mkdir k8s
cd k8s
touch deployment.tml service.yml
```

11. Start Minikube:
```bash
minikube start
```

12. Create Kubernetes Secret:
```bash
kubectl create secret docker-registry ecr-secret \
  --docker-server=<account-id>.dkr.ecr.<region>.amazonaws.com \
  --docker-username=AWS \
  --docker-password="$(aws ecr get-login-password --region <region>)"
  ```

  13. Deploy the Application
  ```bash
  kubectl apply -f deployment.yml
  kubectl apply -f service.yml
  ```

  14. Check the deployment, service, and pods:
  ```bash
  kubectl get deployments
  kubectl get pods
  kubectl get svc
  ```

  15. Access the application:
```bash
minikube service voters-api-svc
```

## Contributions
Contributions and suggestions are welcome.


