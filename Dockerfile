FROM python:3.8-slim

# "Maintainer" está obsoleto, usa LABEL org.opencontainers.image.authors
LABEL Maintainer="hansel_prins10@hotmail.com"

# Definir el directorio de trabajo
WORKDIR /authentication_server_example

# Copiar primero requirements para aprovechar el caché de capas de Docker
COPY requirements.txt .
RUN pip3 install --no-cache-dir --upgrade pip && \
    pip3 install --no-cache-dir -r requirements.txt

# Copiar el código fuente (puedes usar . para copiar todo el contexto)
COPY . .

# Exponer el puerto
EXPOSE 8000

# Como tu archivo es run.py, debe ser 'run:app'
CMD ["gunicorn", "-w", "2", "-b", "0.0.0.0:5000", "run:app"]