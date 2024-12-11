from django.db import models



class DiaSemana(models.Model):
    DIAS = [
        ('lunes', 'Lunes'),
        ('martes', 'Martes'),
        ('miercoles', 'Miércoles'),
        ('jueves', 'Jueves'),
        ('viernes', 'Viernes'),
        ('sabado', 'Sábado'),
        ('domingo', 'Domingo'),
    ]
    rutina = models.ForeignKey(
        'Rutina',
        on_delete=models.CASCADE,
        related_name="dias",
        verbose_name="Rutina"
    )
    dia = models.CharField(max_length=20, choices=DIAS, verbose_name="Día de la Semana")

    def __str__(self):
        return f"{self.rutina.titulo} - {self.dia}"

    class Meta:
        verbose_name = "Día de la Semana"
        verbose_name_plural = "Días de la Semana"
        unique_together = ('rutina', 'dia')