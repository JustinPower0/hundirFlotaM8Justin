FROM php:8.2-apache

# Instalar extensiones necesarias
RUN docker-php-ext-install pdo pdo_mysql

# Copiar los archivos del sitio web
COPY ./Programa /var/www/html/

# Dar permisos a Apache
RUN chmod -R 755 /var/www/html

# Apache ya se inicia automáticamente
# Usar una imagen base de Python 3.9
FROM python:3.9-slim

# Establecer el directorio de trabajo en el contenedor
WORKDIR /app

# Copiar los archivos del proyecto al directorio de trabajo
COPY . /app

# Instalar las dependencias del archivo requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Comando para ejecutar la aplicación principal
CMD ["python", "app.py"]
