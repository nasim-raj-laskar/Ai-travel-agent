# AWS Deployment Guide

## Prerequisites
- AWS CLI configured with appropriate permissions
- Docker installed
- kubectl installed
- eksctl installed
- Helm installed (for Load Balancer Controller)

## Deployment Steps

### 1. Create ECR Repository (if not exists)
```bash
aws ecr create-repository --repository-name streamlit-app --region us-east-1
```

### 2. Build and Push Docker Image
```bash
cd aws-deployment
chmod +x ecr-push.sh
./ecr-push.sh
```

### 3. Setup EKS Cluster
```bash
chmod +x eks-setup.sh
./eks-setup.sh
```

### 4. Deploy Applications
```bash
chmod +x deploy.sh
./deploy.sh
```

### 5. Access Applications
- Kibana: Use NodePort (port 30601) or setup ingress
- Streamlit App: Access via LoadBalancer URL

## Alternative: Terraform Deployment
```bash
cd terraform
terraform init
terraform plan
terraform apply
```

## Monitoring
- Check pod status: `kubectl get pods -n logging`
- View logs: `kubectl logs -f deployment/elasticsearch -n logging`
- Port forward for local access: `kubectl port-forward svc/kibana 5601:5601 -n logging`

## Cleanup
```bash
kubectl delete -f ../
eksctl delete cluster --name ai-travel-agent-cluster --region us-east-1
```