from django.db import models

from apps.adopciones.models import Persona


class Vacuna(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Vacuna'
        verbose_name_plural = 'Vacunas'


class Mascota(models.Model):

    ESPECIE_CHOICES = [
        ('perro', 'Perro'),
        ('gato', 'Gato'),
        ('conejo', 'Conejo'),
        ('ave', 'Ave'),
        ('otro', 'Otro'),
    ]

    SEXO_CHOICES = [
        ('macho', 'Macho'),
        ('hembra', 'Hembra'),
    ]

    ESTADO_CHOICES = [
        ('disponible', 'Disponible'),
        ('en_proceso', 'En proceso de adopción'),
        ('adoptado', 'Adoptado'),
    ]

    nombre = models.CharField(max_length=50)
    especie = models.CharField(max_length=20, choices=ESPECIE_CHOICES, default='perro')
    sexo = models.CharField(max_length=10, choices=SEXO_CHOICES, default='macho')
    edad_aproximada = models.IntegerField()
    fecha_rescate = models.DateField()
    descripcion = models.TextField(blank=True)
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='disponible')
    persona = models.ForeignKey(Persona, null=True, blank=True, on_delete=models.SET_NULL)
    vacuna = models.ManyToManyField(Vacuna, blank=True)

    def __str__(self):
        return '{} ({})'.format(self.nombre, self.get_especie_display())

    class Meta:
        verbose_name = 'Mascota'
        verbose_name_plural = 'Mascotas'
