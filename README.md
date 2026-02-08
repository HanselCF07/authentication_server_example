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

# Cargar la imagen directamente en el clúster (sin registry)
    minikube image load authentication-server-example:v1  # Si usas Minikube
    
    kind load docker-image authentication-server-example:v1 # Si usas Kind

# Create Deployment and Service
    kubectl apply -f k8s-deployment.yaml
    kubectl apply -f k8s-service.yaml

# Configure Ingress (Opcional)
    kubectl apply -f k8s-ingress.yaml

# Activar el Ingress Controller (Opcional)
    minikube addons enable ingress

# View pods
    kubectl get pods
# View servicios
    kubectl get svc

# Reenvío de puertos (La más rápida para pruebas)
    kubectl port-forward --address 0.0.0.0 service/NOMBRE_DE_TU_SERVICIO 8000:8000 (puerto a exponer servidor):(puerto servicio)



