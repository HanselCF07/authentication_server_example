Run With: Python 3.8 Version

# authentication_server_example
Python Flask - authentication server example


# Build the image
docker build -t authentication-server-example:v1 .
docker run -d -p 8000:8000 authentication-server-example:v1

# Run the container in localhost:8000 and inject environment variables
# Remember to create a file with the environment variables used in the App Configuration
docker run -d -p 8000:8000 --env-file .env authentication-server-example:v1


# Test API
curl -X POST http://localhost:8000/api/v1/authentication/user/login \
-H "Content-Type: application/json" \


# Start Minikube (if it is not running)
minikube start --driver=docker

# Create Deployment and Service
kubectl apply -f k8s-deployment.yaml
kubectl apply -f k8s-service.yaml

# Configure Ingress
kubectl apply -f k8s-ingress.yaml


# View pods
kubectl get pods
# View servicios
kubectl get svc



