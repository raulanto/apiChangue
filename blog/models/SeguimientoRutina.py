from django.db import models

class SeguimientoRutina(models.Model):
    rutina_guardada = models.ForeignKey(
        'RutinaGuardada',
        on_delete=models.CASCADE,
        related_name='seguimientos',
        verbose_name="Rutina Guardada"
    )
    fecha = models.DateField(verbose_name="Fecha de Seguimiento")
    ejercicio = models.ForeignKey(
        'Ejercicio',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='seguimientos_rutina',
        verbose_name="Ejercicio"
    )
    comida = models.ForeignKey(
        'Alimentacion',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='seguimientos_rutina',
        verbose_name="Comida"
    )
    habito = models.ForeignKey(
        'Habito',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='seguimientos_rutina',
        verbose_name="Hábito"
    )
    completado = models.BooleanField(default=False, verbose_name="¿Completado?")

    def __str__(self):
        tipos = []
        if self.ejercicio:
            tipos.append(f"Ejercicio: {self.ejercicio.nombre}")
        if self.comida:
            tipos.append(f"Comida: {self.comida.nombre}")
        if self.habito:
            tipos.append(f"Hábito: {self.habito.nombre}")
        return f"Seguimiento ({', '.join(tipos)}) - {self.fecha}"

    class Meta:
        verbose_name = "Seguimiento de Rutina"
        verbose_name_plural = "Seguimientos de Rutinas"
        unique_together = ('rutina_guardada', 'fecha', 'ejercicio', 'comida', 'habito')