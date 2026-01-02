from django import forms
from .models import Coche

class CocheForm(forms.ModelForm):
    class Meta:
        model = Coche
        fields = [
            "marca_modelo",
            "año",
            "kilometraje",
            "precio",
            "combustible",
            "transmision",
            "estado_general",
            "mantenimiento",
            "documentacion",
            "ubicacion",
        ]

        widgets = {
            "marca_modelo": forms.TextInput(attrs={"class": "form-input"}),
            "año": forms.NumberInput(attrs={"class": "form-input"}),
            "kilometraje": forms.NumberInput(attrs={"class": "form-input"}),
            "precio": forms.NumberInput(attrs={"class": "form-input"}),
            "estado_general": forms.Textarea(attrs={"class": "form-textarea"}),
            "mantenimiento": forms.Textarea(attrs={"class": "form-textarea"}),
            "documentacion": forms.Textarea(attrs={"class": "form-textarea"}),
            "ubicacion": forms.TextInput(attrs={"class": "form-input"}),
        }
