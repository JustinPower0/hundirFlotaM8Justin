FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia tu proyecto (HTML, JS, FastAPI, etc.)
COPY . .

# Servir HTML y JS estáticos desde FastAPI
RUN mkdir -p /app/static
COPY ./Programa /app/static

EXPOSE 8080

# FastAPI servirá los estáticos y las rutas del juego
CMD ["uvicorn", "FastApi.main:app", "--host", "0.0.0.0", "--port", "8080"]
