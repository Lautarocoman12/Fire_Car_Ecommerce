from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),

    # Rutas de tu app principal
    path("", include("app.urls")),

    # Rutas de tu app accounts (registro/login propios)
    path("accounts/", include("accounts.urls")),

    # Rutas de allauth (para login con Google y otros proveedores)
    path("accounts/", include("allauth.urls")),
]

# 👇 Necesario para mostrar y guardar imágenes en desarrollo
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
