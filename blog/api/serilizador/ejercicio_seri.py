from rest_framework import serializers
from ...models.Ejercicio import Ejercicio


class EjercicioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ejercicio
        fields = '__all__'
