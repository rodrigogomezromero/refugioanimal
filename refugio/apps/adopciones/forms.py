from django import forms
from apps.adopciones.models import Persona, Solicitud


class PersonaForm(forms.ModelForm):

    class Meta:
        model = Persona
        fields = [
            'nombre',
            'apellidos',
            'edad',
            'telefono',
            'email',
            'domicilio',
        ]
        labels = {
            'nombre': 'Nombre',
            'apellidos': 'Apellidos',
            'edad': 'Edad',
            'telefono': 'Teléfono',
            'email': 'Correo electrónico',
            'domicilio': 'Domicilio',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellidos': forms.TextInput(attrs={'class': 'form-control'}),
            'edad': forms.NumberInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'domicilio': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }


class SolicitudForm(forms.ModelForm):

    class Meta:
        model = Solicitud
        fields = [
            'numero_mascotas',
            'razones',
        ]
        labels = {
            'numero_mascotas': 'Número de mascotas que desea adoptar',
            'razones': 'Razones para adoptar',
        }
        widgets = {
            'numero_mascotas': forms.NumberInput(attrs={'class': 'form-control', 'min': 1}),
            'razones': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }


class SolicitudEstadoForm(forms.ModelForm):

    class Meta:
        model = Solicitud
        fields = [
            'numero_mascotas',
            'razones',
            'estado',
        ]
        labels = {
            'numero_mascotas': 'Número de mascotas',
            'razones': 'Razones para adoptar',
            'estado': 'Estado de la solicitud',
        }
        widgets = {
            'numero_mascotas': forms.NumberInput(attrs={'class': 'form-control', 'min': 1}),
            'razones': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'estado': forms.Select(attrs={'class': 'form-control'}),
        }
