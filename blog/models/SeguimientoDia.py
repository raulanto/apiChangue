from django.db import models

class SeguimientoDia(models.Model):
    dia = models.ForeignKey(
        'DiaSemana',
        on_delete=models.CASCADE,
        related_name="seguimientos",
        verbose_name="Día de la Semana"
    )
    fecha = models.DateField(verbose_name="Fecha de Seguimiento")
    completado = models.BooleanField(default=False, verbose_name="¿Completado?")

    def __str__(self):
        return f"Seguimiento {self.dia.dia} - {self.fecha}"

    class Meta:
        verbose_name = "Seguimiento del Día"
        verbose_name_plural = "Seguimientos de Días"
        unique_together = ('dia', 'fecha')