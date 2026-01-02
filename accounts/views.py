from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from .forms import RegistroForm, LoginForm, PerfilForm

# Página principal
def index(request):
    return render(request, "index.html")

# Dashboard protegido (solo usuarios logueados)
@login_required
def dashboard(request):
    usuario = request.user
    if request.method == 'POST':
        form = PerfilForm(request.POST, request.FILES, instance=usuario)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = PerfilForm(instance=usuario)
    return render(request, "dashboard.html", {"form": form})

# Registro con formulario
def registro(request):
    form = RegistroForm(request.POST or None)
    if form.is_valid():
        usuario = form.save()
        login(request, usuario, backend='django.contrib.auth.backends.ModelBackend')
        return redirect('dashboard')
    return render(request, "register.html", {"form": form})

# Login con formulario
def login_view(request):
    form = LoginForm(request, data=request.POST or None)
    if form.is_valid():
        usuario = form.get_user()
        login(request, usuario, backend='django.contrib.auth.backends.ModelBackend')
        return redirect('dashboard')
    return render(request, "login.html", {"form": form})

# Logout seguro por POST
@require_POST
def logout_view(request):
    logout(request)
    return redirect('index')
