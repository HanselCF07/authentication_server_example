FROM python:3.8-slim

LABEL Mantainer "hansel_prins10@hotmail.com"

WORKDIR /authentication_service

COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY *.py ./

EXPOSE 8000

CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:8000", "app:app"]