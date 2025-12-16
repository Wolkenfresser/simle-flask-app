FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir flask prometheus-flask-exporter

COPY . .

EXPOSE 5000

CMD ["python", "app.py"]
