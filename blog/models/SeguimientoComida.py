from django.db import models
from datetime import date


class SeguimientoComida(models.Model):
    DIAS_SEMANA = [
        ('lunes', 'Lunes'),
        ('martes', 'Martes'),
        ('miercoles', 'Miércoles'),
        ('jueves', 'Jueves'),
        ('viernes', 'Viernes'),
        ('sabado', 'Sábado'),
        ('domingo', 'Domingo'),
    ]

    comida = models.ForeignKey(
        'Alimentacion',  # Asegúrate de que exista el modelo Alimentacion
        on_delete=models.CASCADE,
        related_name='seguimientos_comida',
        verbose_name="Comida"
    )
    dia = models.CharField(
        max_length=10,
        choices=DIAS_SEMANA,
        verbose_name="Día de la semana"
    )
    completado = models.BooleanField(
        default=False,
        verbose_name="Completado",
        help_text="Indica si se consumió la comida según el plan."
    )
    fecha = models.DateField(
        default=date.today,
        verbose_name="Fecha",
        help_text="Fecha en la que se registró el seguimiento."
    )
    observaciones = models.TextField(
        blank=True,
        null=True,
        verbose_name="Observaciones",
        help_text="Notas adicionales sobre la comida."
    )

    def __str__(self):
        return f"{self.comida.nombre_comida} - {self.get_dia_display()} - {'Completado' if self.completado else 'Pendiente'}"

    class Meta:
        verbose_name = "Seguimiento de Comida"
        verbose_name_plural = "Seguimiento de Comidas"
        ordering = ['fecha', 'dia']
        unique_together = ('comida', 'dia', 'fecha')  # Evita duplicados para el mismo registro
