# authentication_server_example
Python Flask - authentication server example



# Construir la imagen
docker build -t flask-app:latest .

# Ejecutar el contenedor en localhost:8000 and inject environment variables
docker run -d -p 8000:8000 --env-file .env --name flask-container flask-app:latest



# Iniciar Minikube (si no está corriendo)
minikube start --driver=docker

# Crear Deployment y Service
kubectl apply -f k8s-deployment.yaml
kubectl apply -f k8s-service.yaml

# Configurar Ingress 
kubectl apply -f k8s-ingress.yaml


# Ver pods
kubectl get pods
# Ver servicios
kubectl get svc


