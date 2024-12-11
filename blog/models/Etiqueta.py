from django.db import models


class Etiqueta(models.Model):
    nombre = models.CharField(max_length=50, unique=True, verbose_name="Nombre de la etiqueta")
    objects = models.Manager()

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Etiqueta"
        verbose_name_plural = "Etiquetas"