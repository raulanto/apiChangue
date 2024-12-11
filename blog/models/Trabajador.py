from django.db import models
from django.contrib.auth.models import User

class Trabajador(models.Model):
    """
    Modelo para registrar trabajadores con datos adicionales y una relación con el usuario de Django.
    """
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name='trabajador', verbose_name="Usuario")
    telefono = models.CharField(max_length=15, verbose_name="Teléfono", blank=True, null=True)
    ciudad = models.CharField(max_length=100, verbose_name="Ciudad")
    edad = models.PositiveIntegerField(verbose_name="Edad")
    foto_cedula = models.ImageField(upload_to='cedulas/', verbose_name="Foto de la Cédula", blank=True, null=True)
    estado_solicitud = models.CharField(
        max_length=20,
        choices=[
            ('en_proceso', 'En Proceso'),
            ('autorizado', 'Autorizado'),
            ('rechazado', 'Rechazado'),
        ],
        default='en_proceso',
        verbose_name="Estado de la Solicitud"
    )
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    fecha_actualizacion = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización")

    def __str__(self):
        return f"{self.usuario.username} - {self.estado_solicitud}"

    class Meta:
        verbose_name = "Trabajador"
        verbose_name_plural = "Trabajadores"
        ordering = ['-fecha_creacion']
