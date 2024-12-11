from rest_framework import serializers
from ...models.Post import Post
from ..serilizador.etiqueta_seri import EtiquetaSerializer
from ...models.Etiqueta import Etiqueta
class PostSerializer(serializers.ModelSerializer):
    #etiquetas = EtiquetaSerializer(many=True, read_only=True)
    class Meta:
        model = Post
        fields = '__all__'






class PostCreateSerializer(serializers.ModelSerializer):


    class Meta:
        model = Post
        fields = ['id', 'titulo', 'contenido', 'autor', 'imagen', 'etiquetas','publicado']

