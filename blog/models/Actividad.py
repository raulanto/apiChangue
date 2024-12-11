from django.db import models

class Actividad(models.Model):
    dia = models.ForeignKey(
        'DiaSemana',
        on_delete=models.CASCADE,
        related_name="actividades",
        verbose_name="Día de la Semana"
    )
    tipo = models.CharField(
        max_length=20,
        choices=[
            ('ejercicio', 'Ejercicio'),
            ('comida', 'Comida'),
            ('habito', 'Hábito'),
        ],
        verbose_name="Tipo de Actividad"
    )
    referencia = models.PositiveIntegerField(verbose_name="ID de la Referencia")
    completado = models.BooleanField(default=False, verbose_name="¿Completado?")

    def __str__(self):
        return f"Actividad {self.tipo} - Día {self.dia.dia}"

    class Meta:
        verbose_name = "Actividad"
        verbose_name_plural = "Actividades"
