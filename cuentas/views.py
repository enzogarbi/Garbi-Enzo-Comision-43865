from django.contrib.auth import login, logout, authenticate  # Importamos las funciones necesarias para manejar la autenticación.
from django.shortcuts import render, redirect  # Importamos las funciones para manejar las respuestas y redirecciones.
from .forms import CustomUserCreationForm, CustomUserChangeForm  # Importamos los formularios para la creación y edición de usuarios.
from django.views import View  # Importamos View para usar clases en nuestras vistas.

# Clase para manejar la página de inicio.
class PaginaInicioView(View):
    def get(self, request):  # Método GET para manejar las solicitudes GET.
        return render(request, 'inicio.html')  # Renderiza la página de inicio.

# Función para manejar el inicio de sesión.
def user_login(request):
    if request.method == 'POST':  # Verificamos si la solicitud es POST.
        username = request.POST['username']  # Obtenemos el nombre de usuario del formulario.
        password = request.POST['password']  # Obtenemos la contraseña del formulario.
        user = authenticate(request, username=username, password=password)  # Autenticamos el usuario.
        if user is not None:  # Si el usuario existe y las credenciales son correctas.
            login(request, user)  # Iniciamos sesión.
            return redirect('Melfa:menu')  # Redirigimos al menú.
    return render(request, 'login.html')  # Renderizamos la página de inicio de sesión si no es una solicitud POST o si falla la autenticación.

# Función para manejar el cierre de sesión.
def user_logout(request):
    logout(request)  # Cerramos la sesión del usuario.
    return redirect('login')  # Redirigimos a la página de inicio de sesión.

# Función para manejar el registro de nuevos usuarios.
def user_register(request):
    if request.method == 'POST':  # Verificamos si la solicitud es POST.
        form = CustomUserCreationForm(request.POST, request.FILES)  # Creamos el formulario con los datos enviados.
        if form.is_valid():  # Validamos el formulario.
            form.save()  # Guardamos el usuario en la base de datos.
            return redirect('cuentas:login')  # Redirigimos a la página de inicio de sesión.
    else:
        form = CustomUserCreationForm()  # Creamos un formulario vacío si no es una solicitud POST.
    return render(request, 'registro.html', {'form': form})  # Renderizamos la página de registro con el formulario.

# Función para manejar la edición del perfil del usuario.
def user_edit(request):
    if request.method == 'POST':  # Verificamos si la solicitud es POST.
        form = CustomUserChangeForm(request.POST, request.FILES, instance=request.user)  # Creamos el formulario con los datos enviados y la instancia actual del usuario.
        if form.is_valid():  # Validamos el formulario.
            form.save()  # Guardamos los cambios en la base de datos.
            return redirect('cuentas:perfil')  # Redirigimos a la página de perfil.
    else:
        form = CustomUserChangeForm(instance=request.user)  # Creamos un formulario con la instancia actual del usuario si no es una solicitud POST.
    return render(request, 'editar.html', {'form': form})  # Renderizamos la página de edición con el formulario.

# Función para manejar la visualización del perfil del usuario.
def user_profile(request):
    return render(request, 'perfil.html')  # Renderizamos la página de perfil.
