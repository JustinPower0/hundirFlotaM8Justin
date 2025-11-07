FROM php:8.2-apache

# Instalar extensiones necesarias
RUN docker-php-ext-install pdo pdo_mysql

# Copiar los archivos del sitio web
COPY ./Programa /var/www/html/

# Dar permisos a Apache
RUN chmod -R 755 /var/www/html

# Imagen base oficial de Python
FROM python:3.11

# Establecer el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar todo el contenido del proyecto al contenedor
COPY . /app

# Instalar FastAPI y Uvicorn (y otras dependencias si tienes un requirements.txt)
RUN pip install fastapi uvicorn

# Exponer el puerto donde correrá el servidor
EXPOSE 8000

# Comando para ejecutar la aplicación FastAPI
CMD ["uvicorn", "FastApi.main:app", "--host", "0.0.0.0", "--port", "8000"]
