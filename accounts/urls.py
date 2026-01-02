# accounts/urls.py
from django.urls import path
from .views import index, registro, login_view, dashboard
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', index, name='index'),
    path('registro/', registro, name='registro'),
    path('login/', login_view, name='login'),
    path('dashboard/', dashboard, name='dashboard'),
    path('logout/', LogoutView.as_view(next_page='index'), name='logout'),
]
