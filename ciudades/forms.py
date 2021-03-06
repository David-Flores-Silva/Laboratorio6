from django import forms
from .models import Ciudad

class CiudadForm(forms.ModelForm):
    class Meta:
        model = Ciudad
        fields = [
            "nombre",
            "pais",
            "departamento",
            "oferta",
            "precio",
        ]