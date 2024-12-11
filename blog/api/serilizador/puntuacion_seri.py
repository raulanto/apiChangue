from rest_framework import serializers
from blog.models.Post import Post, Puntuacion
from django.db import models


def actualizar_puntuacion_post(post):
    """
    Actualiza la puntuación total y el número de puntuaciones de un post.
    """
    puntuaciones = post.puntuaciones.aggregate(
        total=models.Sum('puntuacion'),
        count=models.Count('puntuacion')
    )
    post.puntuacion_total = puntuaciones['total'] or 0
    post.numero_puntuaciones = puntuaciones['count'] or 0
    post.save()






class PuntuacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Puntuacion
        fields = ['id', 'post', 'usuario', 'puntuacion']


    def validate(self, attrs):
        post = attrs.get('post')
        usuario = self.context['request'].user

        # Verifica si ya existe una puntuación para este usuario y post
        if Puntuacion.objects.filter(post=post, usuario=usuario).exists():
            raise serializers.ValidationError("Ya has puntuado este post.")

        return attrs

    def create(self, validated_data):
        puntuacion = super().create(validated_data)
        # Actualiza la puntuación del post
        actualizar_puntuacion_post(puntuacion.post)
        # Asocia el usuario autenticado al registro
        validated_data['usuario'] = self.context['request'].user
        return super().create(validated_data)