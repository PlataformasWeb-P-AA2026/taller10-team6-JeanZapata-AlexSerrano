from django import forms
from .models import Barrio

class BarrioForm(forms.ModelForm):
    class Meta:
        model = Barrio
        fields = ['nombre', 'num_viviendas', 'num_parques', 'num_edificios', 'parroquia']