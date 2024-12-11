from django.db import models

class RutinaGuardada(models.Model):
    consumidor = models.ForeignKey(
        'Consumidor',
        on_delete=models.CASCADE,
        related_name='rutinas_guardadas',
        verbose_name="Consumidor"
    )
    rutina = models.ForeignKey(
        'Rutina',
        on_delete=models.CASCADE,
        related_name='guardada_por',
        verbose_name="Rutina"
    )
    guardada_en = models.DateTimeField(auto_now_add=True, verbose_name="Guardada en")

    def __str__(self):
        return f"Rutina '{self.rutina.titulo}' guardada por {self.consumidor.nombre}"

    class Meta:
        verbose_name = "Rutina Guardada"
        verbose_name_plural = "Rutinas Guardadas"
        unique_together = ('consumidor', 'rutina')  # Evita que un consumidor guarde la misma rutina más de una vez
