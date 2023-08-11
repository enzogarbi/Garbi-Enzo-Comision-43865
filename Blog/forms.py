# Primero, importamos la biblioteca "forms" de Django para trabajar con formularios.
# También importamos los modelos "Blog" y "Page" desde el archivo actual del directorio (indicado con el punto).
from django import forms
from .models import Blog, Page

# Creamos una clase llamada "BlogForm" que hereda de "forms.ModelForm".
# Esta clase se utilizará para crear un formulario basado en el modelo "Blog".
class BlogForm(forms.ModelForm):
    # Dentro de la clase, definimos una subclase "Meta" que contiene información adicional sobre el formulario.
    class Meta:
        # Indicamos que el modelo en el que se basa el formulario es "Blog".
        model = Blog
        # Especificamos los campos del modelo que queremos incluir en el formulario.
        fields = ['title', 'subtitle', 'body', 'author', 'image'] 
        # Definimos las etiquetas que se mostrarán junto a cada campo en el formulario.
        labels = {
            'title': 'Título',
            'subtitle': 'Subtítulo',
            'body': 'Cuerpo',
            'author': 'Autor',
            'image': 'Imagen',
        }

# De manera similar, creamos una clase "PageForm" que se basa en el modelo "Page".
# Esta clase define un formulario para crear o editar páginas.
class PageForm(forms.ModelForm):
    # Nuevamente, usamos una subclase "Meta" para contener la información adicional del formulario.
    class Meta:
        # Indicamos que el modelo en el que se basa el formulario es "Page".
        model = Page
        # Especificamos los campos del modelo que queremos incluir en el formulario.
        fields = ['title', 'content']
