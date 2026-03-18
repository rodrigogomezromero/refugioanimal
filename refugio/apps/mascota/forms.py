from django import forms
from apps.mascota.models import Mascota


class MascotaForm(forms.ModelForm):

    class Meta:
        model = Mascota
        fields = [
            'nombre',
            'especie',
            'sexo',
            'edad_aproximada',
            'fecha_rescate',
            'descripcion',
            'estado',
            'persona',
            'vacuna',
        ]
        labels = {
            'nombre': 'Nombre',
            'especie': 'Especie',
            'sexo': 'Sexo',
            'edad_aproximada': 'Edad aproximada (meses)',
            'fecha_rescate': 'Fecha de rescate',
            'descripcion': 'Descripción',
            'estado': 'Estado',
            'persona': 'Adoptante',
            'vacuna': 'Vacunas aplicadas',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'especie': forms.Select(attrs={'class': 'form-control'}),
            'sexo': forms.Select(attrs={'class': 'form-control'}),
            'edad_aproximada': forms.NumberInput(attrs={'class': 'form-control', 'min': 0}),
            'fecha_rescate': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'estado': forms.Select(attrs={'class': 'form-control'}),
            'persona': forms.Select(attrs={'class': 'form-control'}),
            'vacuna': forms.CheckboxSelectMultiple(),
        }
