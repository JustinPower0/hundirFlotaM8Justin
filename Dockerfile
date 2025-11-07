# Imagen base oficial de Python
FROM python:3.12-slim

# Establecer directorio de trabajo en el contenedor
WORKDIR /app

# Copiar requirements.txt y otros archivos necesarios
COPY requirements.txt .

# Instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copiar toda la carpeta "programa" al contenedor
COPY . .


# Exponer el puerto que usará FastAPI
EXPOSE 8000

# Comando para ejecutar FastAPI con uvicorn
CMD ["uvicorn", "fastapi.main:app", "--host", "0.0.0.0", "--port", "8000"]
