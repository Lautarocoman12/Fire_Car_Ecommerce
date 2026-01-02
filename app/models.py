from django.db import models
from accounts.models import UsuarioPersonalizado  # importamos tu modelo de usuario

class Coche(models.Model):

    COMBUSTIBLE_CHOICES = [
        ('nafta', 'Nafta'),
        ('diesel', 'Diésel'),
        ('hibrido', 'Híbrido'),
        ('electrico', 'Eléctrico'),
    ]

    TRANSMISION_CHOICES = [
        ('manual', 'Manual'),
        ('automatica', 'Automática'),
    ]

    usuario = models.ForeignKey(
        UsuarioPersonalizado,
        on_delete=models.CASCADE,
        related_name='coches',
        null=True,
        blank=True
    )

    marca_modelo = models.CharField(max_length=100)
    año = models.IntegerField()
    kilometraje = models.IntegerField()
    precio = models.DecimalField(max_digits=12, decimal_places=2)

    combustible = models.CharField(max_length=20, choices=COMBUSTIBLE_CHOICES)
    transmision = models.CharField(max_length=20, choices=TRANSMISION_CHOICES)

    estado_general = models.TextField()
    mantenimiento = models.TextField()
    documentacion = models.TextField()

    ubicacion = models.CharField(max_length=100)
    fecha_publicacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.marca_modelo} - {self.año}"


class FotoCoche(models.Model):
    coche = models.ForeignKey(Coche, related_name='fotos', on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='coches/')

    def __str__(self):
        return f"Foto de {self.coche.marca_modelo}"
