from django.contrib.auth.models import User
from django.db import models

class Consumidor(models.Model):
    usuario = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='consumidor',
        verbose_name="Usuario de Django",
        help_text="Usuario autenticado asociado al consumidor.",
        blank=True,
        null=True
    )
    nombre = models.CharField(max_length=255, verbose_name="Nombre")
    apellidos = models.CharField(max_length=255, verbose_name="Apellidos")
    correo_electronico = models.EmailField(unique=True, verbose_name="Correo electrónico")
    preferencias = models.TextField(
        verbose_name="Preferencias",
        blank=True,
        help_text="Describe las preferencias de contenido del consumidor, como temas de interés."
    )
    registrado_en = models.DateTimeField(auto_now_add=True, verbose_name="Registrado en")
    actualizado_en = models.DateTimeField(auto_now=True, verbose_name="Actualizado en")

    def __str__(self):
        return f"{self.nombre} {self.apellidos}"

    class Meta:
        verbose_name = "Consumidor"
        verbose_name_plural = "Consumidores"
        ordering = ['registrado_en']
