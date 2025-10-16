#!/bin/bash

# Load AWS credentials
source .env.aws
export AWS_ACCESS_KEY_ID
export AWS_SECRET_ACCESS_KEY
export AWS_DEFAULT_REGION

# Deploy ELK Stack and Application to EKS
echo "Deploying Elasticsearch..."
kubectl apply -f ../elasticsearch.yaml

echo "Waiting for Elasticsearch to be ready..."
kubectl wait --for=condition=available --timeout=300s deployment/elasticsearch -n logging

echo "Deploying Logstash..."
kubectl apply -f ../logstash.yaml

echo "Waiting for Logstash to be ready..."
kubectl wait --for=condition=available --timeout=300s deployment/logstash -n logging

echo "Deploying Filebeat..."
kubectl apply -f ../filebeat.yaml

echo "Deploying Kibana..."
kubectl apply -f ../kibana.yaml

echo "Waiting for Kibana to be ready..."
kubectl wait --for=condition=available --timeout=300s deployment/kibana -n logging

echo "Deploying Streamlit application..."
kubectl apply -f ../k8s-deployment.yaml

echo "Getting service URLs..."
echo "Kibana URL:"
kubectl get svc kibana -n logging -o jsonpath='{.status.loadBalancer.ingress[0].hostname}:30601'
echo ""
echo "Streamlit App URL:"
kubectl get svc streamlit-service -o jsonpath='{.status.loadBalancer.ingress[0].hostname}'
echo ""

echo "Deployment complete!"