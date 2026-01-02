from django.urls import path
from .views import index, login_view, registro, dashboard, marketplace, publicar_producto, detalle_producto, comovender

urlpatterns = [
    path("", index, name="index"),
    path("login/", login_view, name="login"),
    path("registro/", registro, name="registro"),
    path("dashboard/", dashboard, name="dashboard"),
    path("marketplace/", marketplace, name="marketplace"),
    path("marketplace/publicar/", publicar_producto, name="publicar_producto"),
    path("marketplace/<int:pk>/", detalle_producto, name="detalle_producto"),
    path("comovender/", comovender, name="comovender"),
]
