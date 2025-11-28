from django import forms
from .models import Dueño, Mascota, Estadia

class DueñoForm(forms.ModelForm):
    class Meta:
        model = Dueño
        fields = ['nombre', 'telefono', 'email']

class MascotaForm(forms.ModelForm):
    class Meta:
        model = Mascota
        fields = ['nombre', 'especie', 'raza', 'edad', 'dueño'] 

class EstadiaForm(forms.ModelForm):
    class Meta:
        model = Estadia
        fields = ['mascota', 'dueño', 'fecha_inicio', 'fecha_fin', 'observaciones']