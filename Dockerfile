# Imagen base de Python
FROM python:3.11-slim

# Directorio de trabajo
WORKDIR /app

# Copiar dependencias
COPY requirements.txt .

# Instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el proyecto FastAPI
COPY FastApi ./FastApi
COPY data ./data

# Asegurar que FastApi sea un paquete
RUN touch FastApi/__init__.py

# Exponer el puerto de FastAPI
EXPOSE 8080

# Comando para ejecutar FastAPI
CMD ["uvicorn", "FastApi.main:app", "--host", "0.0.0.0", "--port", "8080"]
