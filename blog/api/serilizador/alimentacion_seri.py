from rest_framework import serializers
from ...models.Alimentacion import Alimentacion


class AlimentacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alimentacion
        fields = [
            'id',
            'autor',
            'nombre_comida',
            'descripcion',
            'horario',
            'calorias',
            'proteinas',
            'carbohidratos',
            'grasas',
            'nivel_importancia',
            'fecha_creacion',
            'fecha_actualizacion',
        ]
        read_only_fields = ['id', 'fecha_creacion', 'fecha_actualizacion']