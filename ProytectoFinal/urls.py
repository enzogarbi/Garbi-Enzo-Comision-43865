
from django.contrib import admin
from django.urls import include, path
from cuentas.views import PaginaInicioView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cuentas/', include('cuentas.urls')),
    path('', PaginaInicioView.as_view(), name='inicio'),
    path('Melfa/', include('Melfa.urls')), # Corregido aquí
    path('Blog/', include('Blog.urls', namespace='Blog')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


