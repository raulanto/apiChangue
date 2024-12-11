from rest_framework import serializers
from ...models.Rutina import Rutina


class RutinaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rutina
        fields = '__all__'
