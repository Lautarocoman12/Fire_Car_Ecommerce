from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Coche, FotoCoche
from .forms import CocheForm
from accounts.forms import PerfilForm
from accounts.models import UsuarioPersonalizado

# ----------------------
# PÁGINAS BÁSICAS
# ----------------------

def index(request):
    return render(request, "index.html")

def login_view(request):
    return render(request, "login.html")

def registro(request):
    return render(request, "register.html")

@login_required
def dashboard(request):
    usuario = request.user
    form = PerfilForm(request.POST or None, request.FILES or None, instance=usuario)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('dashboard')

    publicaciones = Coche.objects.filter(usuario=usuario).order_by("-fecha_publicacion")

    return render(request, "dashboard.html", {
        "form": form,
        "publicaciones": publicaciones
    })

def comovender(request):
    return render(request, "comovender.html")

# ----------------------
# MARKETPLACE + FILTROS
# ----------------------

def marketplace(request):
    productos = Coche.objects.all().order_by("-fecha_publicacion")

    combustible = request.GET.get("combustible")
    transmision = request.GET.get("transmision")

    if combustible:
        productos = productos.filter(combustible=combustible)

    if transmision:
        productos = productos.filter(transmision=transmision)

    return render(request, "marketplace.html", {
        "productos": productos
    })

# ----------------------
# PUBLICAR PRODUCTO (solo logueados)
# ----------------------

@login_required
def publicar_producto(request):
    if request.method == "POST":
        form = CocheForm(request.POST, request.FILES)  # ✅ incluir request.FILES
        fotos = request.FILES.getlist("fotos")

        if form.is_valid():
            coche = form.save(commit=False)
            coche.usuario = request.user  # vincular al usuario logueado
            coche.save()

            for foto in fotos:
                FotoCoche.objects.create(
                    coche=coche,
                    imagen=foto
                )

            return redirect("dashboard")
    else:
        form = CocheForm()

    return render(request, "publicar_producto.html", {
        "form": form
    })

# ----------------------
# DETALLE DEL PRODUCTO
# ----------------------

def detalle_producto(request, pk):
    producto = get_object_or_404(Coche, pk=pk)
    return render(request, "detalle_producto.html", {
        "producto": producto
    })
from django.db.models import Q

def marketplace(request):
    productos = Coche.objects.all().order_by("-fecha_publicacion")

    # 🔍 Buscador
    query = request.GET.get("q")
    if query:
        productos = productos.filter(
            Q(marca_modelo__icontains=query) |
            Q(ubicacion__icontains=query)
        )

    # ⛽ Filtros
    combustible = request.GET.get("combustible")
    transmision = request.GET.get("transmision")

    if combustible:
        productos = productos.filter(combustible=combustible)

    if transmision:
        productos = productos.filter(transmision=transmision)

    # 💰 Precio
    precio_min = request.GET.get("precio_min")
    precio_max = request.GET.get("precio_max")

    if precio_min:
        productos = productos.filter(precio__gte=precio_min)

    if precio_max:
        productos = productos.filter(precio__lte=precio_max)

    return render(request, "marketplace.html", {
        "productos": productos,
        "query": query
    })
