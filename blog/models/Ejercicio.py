from django.db import models
from django.contrib.auth.models import User


class Ejercicio(models.Model):
    autor = models.ForeignKey(User, on_delete=models.CASCADE, related_name="ejercicioAutor", verbose_name="Autor")

    nombre = models.CharField(max_length=100, verbose_name="Nombre del ejercicio")
    descripcion = models.TextField(blank=True, null=True, verbose_name="Descripción del ejercicio")
    duracion = models.PositiveIntegerField(verbose_name="Duración (en minutos)",
                                           help_text="Duración aproximada del ejercicio")
    repeticiones = models.PositiveIntegerField(verbose_name="Número de repeticiones",
                                               help_text="Cantidad de repeticiones recomendadas")
    nivel_dificultad = models.CharField(
        max_length=50,
        choices=[
            ('básico', 'Básico'),
            ('intermedio', 'Intermedio'),
            ('avanzado', 'Avanzado'),
        ],
        default='básico',
        verbose_name="Nivel de dificultad"
    )
    grupo_muscular = models.CharField(
        max_length=50,
        choices=[
            ('piernas', 'Piernas'),
            ('brazos', 'Brazos'),
            ('espalda', 'Espalda'),
            ('pecho', 'Pecho'),
            ('core', 'Core'),
            ('completo', 'Cuerpo completo'),
        ],
        verbose_name="Grupo muscular principal"
    )
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    fecha_actualizacion = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización")

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Ejercicio"
        verbose_name_plural = "Ejercicios"
        ordering = ['-fecha_creacion']
