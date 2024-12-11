from rest_framework import serializers
from django.contrib.auth.models import User
from ...models.Trabajador import Trabajador

class UserSerializer(serializers.ModelSerializer):
    """
    Serializador para manejar datos del modelo User.
    """
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'first_name', 'last_name', 'email')
        extra_kwargs = {
            'password': {'write_only': True},  # Oculta la contraseña al leer
        }

    def create(self, validated_data):
        """
        Crea un usuario con la contraseña encriptada.
        """
        user = User.objects.create_user(**validated_data)
        return user


class TrabajadorSerializer(serializers.ModelSerializer):
    """
    Serializador para manejar datos del modelo Trabajador.
    """
    usuario = UserSerializer()  # Relación con el usuario

    class Meta:
        model = Trabajador
        fields = (
            'id',
            'usuario',
            'telefono',
            'ciudad',
            'edad',
            'foto_cedula',
            'estado_solicitud',
        )
        read_only_fields = ('estado_solicitud',)  # El estado se inicializa como 'en_proceso'

    def create(self, validated_data):
        """
        Crea tanto el usuario como el trabajador asociado.
        """
        usuario_data = validated_data.pop('usuario')  # Extraer datos del usuario
        usuario = UserSerializer().create(usuario_data)  # Crear el usuario
        trabajador = Trabajador.objects.create(usuario=usuario, **validated_data)  # Crear el trabajador
        return trabajador
