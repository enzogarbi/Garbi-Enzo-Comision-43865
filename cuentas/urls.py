from django.urls import path
from . import views
from .views import user_profile, PaginaInicioView

app_name = 'cuentas'

urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('registro/', views.user_register, name='registro'),
    path('editar/', views.user_edit, name='editar'),
    path('perfil/', user_profile, name='perfil'),
    path('inicio/', PaginaInicioView.as_view(), name='inicio'),
]