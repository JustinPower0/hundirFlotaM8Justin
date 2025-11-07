# Imagen base de Python
FROM python:3.12-slim

# Directorio de trabajo
WORKDIR /app

# Copiar requirements e instalar dependencias
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar todo el proyecto al contenedor
COPY . .

# Exponer el puerto que uvicorn usará
EXPOSE 8000

# Ejecutar uvicorn
CMD ["uvicorn", "fastapi.main:app", "--host", "0.0.0.0", "--port", "8000"]
