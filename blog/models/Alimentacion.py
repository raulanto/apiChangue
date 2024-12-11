from django.db import models
from django.contrib.auth.models import User


class Alimentacion(models.Model):
    autor = models.ForeignKey(User, on_delete=models.CASCADE, related_name="habitosautor", verbose_name="Autor")

    nombre_comida = models.CharField(
        max_length=100,
        verbose_name="Nombre de la comida",
        help_text="Por ejemplo, Desayuno, Almuerzo, Cena, Merienda."
    )
    descripcion = models.TextField(
        blank=True,
        null=True,
        verbose_name="Descripción",
        help_text="Detalles adicionales sobre esta comida o dieta."
    )
    horario = models.TimeField(verbose_name="Horario", help_text="Hora recomendada para consumir esta comida.")
    calorias = models.PositiveIntegerField(
        verbose_name="Calorías (kcal)",
        help_text="Cantidad aproximada de calorías."
    )
    proteinas = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        verbose_name="Proteínas (g)",
        help_text="Gramos aproximados de proteínas."
    )
    carbohidratos = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        verbose_name="Carbohidratos (g)",
        help_text="Gramos aproximados de carbohidratos."
    )
    grasas = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        verbose_name="Grasas (g)",
        help_text="Gramos aproximados de grasas."
    )
    nivel_importancia = models.CharField(
        max_length=50,
        choices=[
            ('baja', 'Baja'),
            ('media', 'Media'),
            ('alta', 'Alta'),
        ],
        default='media',
        verbose_name="Nivel de importancia"
    )
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    fecha_actualizacion = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización")

    def __str__(self):
        return f"{self.nombre_comida} - {self.horario}"

    class Meta:
        verbose_name = "Alimentación"
        verbose_name_plural = "Alimentaciones"
        ordering = ['horario']
