FROM php:8.2-apache

# Instalar extensiones necesarias
RUN docker-php-ext-install pdo pdo_mysql

# Copiar los archivos del sitio web
COPY ./Programa /var/www/html/

# Dar permisos a Apache
RUN chmod -R 755 /var/www/html

# Imagen base
FROM python:3.11-slim

# Directorio de trabajo
WORKDIR /app

# Copiar dependencias
COPY requirements.txt ./

# Instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copiar todo el proyecto
COPY . .

# Exponer el puerto 8080
EXPOSE 8080

# Comando para ejecutar FastAPI
CMD ["uvicorn", "FastApi.main:app", "--host", "0.0.0.0", "--port", "8080"]
