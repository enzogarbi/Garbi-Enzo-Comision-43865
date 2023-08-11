from django.contrib.auth.models import AbstractUser  # Importamos AbstractUser, que contiene los campos básicos de un usuario.
from django.db import models  # Importamos models para definir el modelo personalizado.

# Definimos una clase CustomUser que hereda de AbstractUser.
# Esto significa que tiene todos los campos y métodos que proporciona Django por defecto para un usuario.
class CustomUser(AbstractUser):
    # Definimos un campo adicional llamado 'avatar', que es una imagen.
    # 'upload_to' especifica en qué carpeta se guardarán las imágenes del avatar en el servidor.
    # 'null=True' y 'blank=True' significa que este campo es opcional, tanto a nivel de base de datos como a nivel de formulario.
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
