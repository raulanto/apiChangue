from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    titulo = models.CharField(max_length=200, unique=True, verbose_name="Título")

    autor = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts", verbose_name="Autor")
    contenido = models.TextField(verbose_name="Contenido")
    imagen = models.ImageField(upload_to='posts/', blank=True, null=True, verbose_name="Imagen destacada")
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    fecha_actualizacion = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización")
    publicado = models.BooleanField( verbose_name="Publicado")
    etiquetas = models.ManyToManyField('Etiqueta', blank=True, related_name="posts", verbose_name="Etiquetas")
    puntuacion_total = models.PositiveIntegerField(default=0, verbose_name="Puntuación total")
    numero_puntuaciones = models.PositiveIntegerField(default=0, verbose_name="Número de puntuaciones")


    @property
    def promedio_puntuacion(self):
        """
        Calcula el promedio de las puntuaciones.
        """
        if self.numero_puntuaciones == 0:
            return 0
        return round(self.puntuacion_total / self.numero_puntuaciones, 2)

    def __str__(self):
        return self.titulo



    class Meta:
        verbose_name = "Publicación"
        verbose_name_plural = "Publicaciones"
        ordering = ['-fecha_creacion']


class Puntuacion(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="puntuaciones", verbose_name="Post")
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Usuario")
    puntuacion = models.PositiveIntegerField(verbose_name="Puntuación", help_text="De 1 a 5.")

    class Meta:
        unique_together = ('post', 'usuario')  # Un usuario solo puede puntuar un post una vez.
        verbose_name = "Puntuación"
        verbose_name_plural = "Puntuaciones"

    def __str__(self):
        return f"{self.usuario.username} - {self.post.titulo} - {self.puntuacion}"