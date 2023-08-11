from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):  # Heredamos la Meta clase de UserCreationForm
        model = CustomUser  # Usamos nuestro modelo personalizado de usuario
        # Estos son los campos que aparecerán en el formulario para crear un usuario nuevo
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'avatar')

class CustomUserChangeForm(UserChangeForm):
    class Meta:  # Heredamos la Meta clase de UserChangeForm
        model = CustomUser  # Usamos nuestro modelo personalizado de usuario
        # Estos son los campos que aparecerán en el formulario para actualizar un usuario existente
        fields = ('username', 'first_name', 'last_name', 'email', 'avatar')
