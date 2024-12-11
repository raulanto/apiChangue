from django.db import models
from django.contrib.auth.models import User

class Habito(models.Model):
    autor = models.ForeignKey(User, on_delete=models.CASCADE, related_name="habitosEjercicio", verbose_name="Autor")
    nombre = models.CharField(max_length=100, verbose_name="Nombre del hábito")
    descripcion = models.TextField(blank=True, null=True, verbose_name="Descripción del hábito")
    frecuencia = models.CharField(
        max_length=50,
        choices=[
            ('diario', 'Diario'),
            ('semanal', 'Semanal'),
            ('mensual', 'Mensual'),
        ],
        default='diario',
        verbose_name="Frecuencia"
    )
    duracion_estimada = models.PositiveIntegerField(
        verbose_name="Duración estimada (en minutos)",
        help_text="Tiempo estimado para realizar el hábito"
    )
    importancia = models.CharField(
        max_length=50,
        choices=[
            ('baja', 'Baja'),
            ('media', 'Media'),
            ('alta', 'Alta'),
        ],
        default='media',
        verbose_name="Importancia del hábito"
    )
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    fecha_actualizacion = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización")

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Hábito"
        verbose_name_plural = "Hábitos"
        ordering = ['-fecha_creacion']
