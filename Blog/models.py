# Importamos el módulo "models" de Django, que nos permite trabajar con modelos en la base de datos.
from django.db import models

# Creamos una clase "Blog" que hereda de "models.Model". Esto define una tabla "Blog" en la base de datos.
class Blog(models.Model):
    # Definimos los campos de la tabla, especificando su tipo y restricciones.
    title = models.CharField(max_length=200)        # Campo para el título, con una longitud máxima de 200 caracteres.
    subtitle = models.CharField(max_length=200)     # Campo para el subtítulo, con una longitud máxima de 200 caracteres.
    body = models.TextField()                       # Campo para el cuerpo del blog, que puede contener mucho texto.
    author = models.CharField(max_length=100)       # Campo para el autor, con una longitud máxima de 100 caracteres.
    date = models.DateField(auto_now_add=True)      # Campo para la fecha, se configura automáticamente cuando se crea el objeto.
    image = models.ImageField(upload_to='blog_images/') # Campo para la imagen, las imágenes se guardarán en el directorio 'blog_images/'.

    # Definimos una función especial llamada "__str__" que retorna una representación en cadena del objeto.
    # En este caso, la representación será el título del blog.
    def __str__(self):
        return self.title

# Creamos una clase similar para una tabla "Page" en la base de datos.
class Page(models.Model):
    title = models.CharField(max_length=200)        # Campo para el título, con una longitud máxima de 200 caracteres.
    content = models.TextField()                   # Campo para el contenido de la página, que puede contener mucho texto.

    # Nuevamente, definimos una función "__str__" para retornar una representación en cadena del objeto.
    # Aquí, la representación será el título de la página.
    def __str__(self):
        return self.title
