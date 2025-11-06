FROM php:8.2-apache

# Instalar PDO MySQL
RUN docker-php-ext-install pdo pdo_mysql

# Copiar tu sitio a la carpeta pública de Apache
COPY ./public /var/www/html/