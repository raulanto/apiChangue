from django.db import models
from django.contrib.auth.models import User
from .Post import Post


class Comentario(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comentarios", verbose_name="Publicación")
    autor = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comentarios", verbose_name="Autor")
    texto = models.TextField(verbose_name="Comentario")
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    objects = models.Manager()

    def __str__(self):
        return f"Comentario de {self.autor} en {self.post.titulo}"

    class Meta:
        verbose_name = "Comentario"
        verbose_name_plural = "Comentarios"
        ordering = ['-fecha_creacion']

