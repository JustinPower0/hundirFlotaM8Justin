# Imagen base
FROM python:3.11-slim

# Directorio de trabajo
WORKDIR /app

# Copiar dependencias
COPY requirements.txt .

# Instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copiar todo el proyecto
COPY . .

# Exponer el puerto
EXPOSE 8080

# Comando para iniciar FastAPI
CMD ["uvicorn", "FastApi.main:app", "--host", "0.0.0.0", "--port", "8080"]
