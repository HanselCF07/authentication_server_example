# Run With: Python 3.8 Version

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

# Upload the image directly to the cluster (without registry)
    minikube image load authentication-server-example:v1  # Si usas Minikube
    
    kind load docker-image authentication-server-example:v1 # Si usas Kind

# Create Deployment and Service
    kubectl apply -f k8s-deployment.yaml
    kubectl apply -f k8s-service.yaml

# Configure Ingress
    kubectl apply -f k8s-ingress.yaml

# Activar el Ingress Controller (minikube)
    minikube addons enable ingress

# View pods
    kubectl get pods
# View servicios
    kubectl get svc

# Remember to modify the nginx configuration to send requests to the cluster's Ingress server.

# Port forwarding (Fastest for testing)
    kubectl port-forward --address 0.0.0.0 service/SERVICE_NAME 8000:8000 (PORT_EXPOSED):(PORT_SERVICE)


