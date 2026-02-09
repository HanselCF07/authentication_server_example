# Run With: Python 3.8 Version

# authentication_server_example
    Python Flask - authentication server example


# Build the image
    docker build --no-cache -t authentication-server-example:v1 .

# Inspect Docker Img
    docker inspect authentication-server-example:v1 | grep ExposedPorts -A 5

# Run Docker img
    docker run -d -p 5000:5000 authentication-server-example:v1



# Run the container in localhost:8000 and inject environment variables
# Remember to create a file with the environment variables used in the App Configuration
    docker run -d -p 5000:5000 --env-file .env authentication-server-example:v1

# Test API
    curl -X POST http://localhost:5000/api/v1/authentication/user/login \
    -H "Content-Type: application/json" \


# Start Minikube (if it is not running)
    minikube start --driver=docker

# Al ejecutar el siguiente comando, tu terminal actual enviará las imágenes directamente al clúster:
    eval $(minikube docker-env)

# Ver iamgenes cargadas en minikube
    minikube image ls

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
    kubectl port-forward --address 0.0.0.0 service/SERVICE_NAME 5000:5000 (PORT_EXPOSED):(PORT_SERVICE)


