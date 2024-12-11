from django.db import models
from datetime import date
from django.contrib.auth.models import User


class SeguimientoEjercicio(models.Model):
    autor = models.ForeignKey(User, on_delete=models.CASCADE, related_name="seguimientoejercicio", verbose_name="Autor",
                              blank=True, null=True)

    DIAS_SEMANA = [
        ('lunes', 'Lunes'),
        ('martes', 'Martes'),
        ('miercoles', 'Miércoles'),
        ('jueves', 'Jueves'),
        ('viernes', 'Viernes'),
        ('sabado', 'Sábado'),
        ('domingo', 'Domingo'),
    ]

    ejercicio = models.ForeignKey(
        'Ejercicio',
        on_delete=models.CASCADE,
        related_name='seguimientos_ejercicio',  # Cambiar este related_name
        verbose_name="Ejercicio"
    )
    dia = models.CharField(
        max_length=10,
        choices=DIAS_SEMANA,
        verbose_name="Día de la semana"
    )
    completado = models.BooleanField(
        default=False,
        verbose_name="Completado",
        help_text="Indica si el ejercicio fue realizado."
    )
    fecha = models.DateField(
        default=date.today,
        verbose_name="Fecha",
        help_text="Fecha en la que se programó el ejercicio."
    )
    observaciones = models.TextField(
        blank=True,
        null=True,
        verbose_name="Observaciones",
        help_text="Notas adicionales sobre el ejercicio."
    )

    def __str__(self):
        return f"{self.ejercicio.nombre} - {self.get_dia_display()} - {'Completado' if self.completado else 'Pendiente'}"

    class Meta:
        verbose_name = "Seguimiento de Ejercicio"
        verbose_name_plural = "Seguimiento de Ejercicios"
        ordering = ['fecha', 'dia']
        unique_together = ('ejercicio', 'dia', 'fecha')  # Evita duplicados para el mismo ejercicio en el mismo día
