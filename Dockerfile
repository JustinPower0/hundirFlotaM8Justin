FROM python:3.11

WORKDIR /app

# Copia todo el proyecto
COPY . /app

# Instala dependencias
RUN pip install --no-cache-dir fastapi uvicorn

# Expone el puerto 8080
EXPOSE 8080

# Arranca FastAPI automáticamente
CMD ["uvicorn", "FastApi.main:app", "--host", "0.0.0.0", "--port", "8080"]
