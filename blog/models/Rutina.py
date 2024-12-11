from django.db import models

class Rutina(models.Model):
    titulo = models.CharField(
        max_length=255,
        verbose_name="Título",
        help_text="Título descriptivo de la rutina."
    )
    ejercicios = models.ManyToManyField(
        'blog.Ejercicio',
        related_name='rutinas',
        verbose_name="Ejercicios",
        blank=True
    )
    habitos = models.ManyToManyField(
        'blog.Habito',
        related_name='rutinas',
        verbose_name="Hábitos",
        blank=True
    )
    comidas = models.ManyToManyField(
        'blog.Alimentacion',
        related_name='rutinas',
        verbose_name="Comidas",
        blank=True
    )
    nutriologo = models.ForeignKey(
        'blog.Trabajador',  # Asume que el modelo Trabajador representa al nutriólogo
        on_delete=models.CASCADE,
        related_name='rutinas',
        verbose_name="Nutriólogo"
    )
    post = models.OneToOneField(
        'blog.Post',
        on_delete=models.CASCADE,
        related_name='rutina',
        verbose_name="Post asociado",
        help_text="Post donde se comparte esta rutina.",
        blank=True,
        null=True
    )
    creado_en = models.DateTimeField(auto_now_add=True, verbose_name="Creado en")
    actualizado_en = models.DateTimeField(auto_now=True, verbose_name="Actualizado en")

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = "Rutina"
        verbose_name_plural = "Rutinas"
        ordering = ['creado_en']
