from django.db import models


class Persona(models.Model):

    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=70)
    edad = models.IntegerField()
    telefono = models.CharField(max_length=12)
    email = models.EmailField()
    domicilio = models.TextField()

    def __str__(self):
        return '{} {}'.format(self.nombre, self.apellidos)

    class Meta:
        verbose_name = 'Persona'
        verbose_name_plural = 'Personas'


class Solicitud(models.Model):

    ESTADO_CHOICES = [
        ('pendiente', 'Pendiente'),
        ('aprobada', 'Aprobada'),
        ('rechazada', 'Rechazada'),
    ]

    persona = models.ForeignKey(Persona, null=True, blank=True, on_delete=models.CASCADE)
    numero_mascotas = models.IntegerField()
    razones = models.TextField()
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='pendiente')
    fecha_solicitud = models.DateField(auto_now_add=True, null=True)

    def __str__(self):
        return 'Solicitud #{} - {}'.format(self.id, self.persona)

    class Meta:
        verbose_name = 'Solicitud de adopción'
        verbose_name_plural = 'Solicitudes de adopción'
