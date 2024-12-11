from rest_framework import serializers
from ...models.Habitos import Habito


class HabitosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habito
        fields = '__all__'
