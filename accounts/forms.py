# accounts/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import UsuarioPersonalizado

class RegistroForm(UserCreationForm):
    class Meta:
        model = UsuarioPersonalizado
        fields = ['nombre', 'apellido', 'email', 'password1', 'password2']

class LoginForm(AuthenticationForm):
    username = forms.EmailField(label='Email')

class PerfilForm(forms.ModelForm):
    class Meta:
        model = UsuarioPersonalizado
        fields = ['nombre', 'apellido', 'email', 'telefono', 'foto_perfil']