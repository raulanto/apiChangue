from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import (
    ListModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
    DestroyModelMixin
)
from rest_framework.generics import CreateAPIView

from ...models.Habitos import Habito
from ..serilizador.habitos_seri import HabitosSerializer


class HabitosViewSet(
    ListModelMixin,
    RetrieveModelMixin,
    DestroyModelMixin,
    UpdateModelMixin,
    GenericViewSet
):
    queryset = Habito.objects.all()

    serializer_class = HabitosSerializer

    # filter_backends = [DjangoFilterBackend,filters.SearchFilter]
    # filterset_fields = ['usuario']

    # def update(self, request, *args, **kwargs):
    #     self.serializer_class = ProductoUpdateSerializer
    #     response = super().update(request, *args, **kwargs)
    #
    #     # # Registra el cambio
    #     # objeto = self.get_object()
    #     # mensaje = "Producto actualizado"
    #     # registrarCambio(request, objeto, mensaje)
    #     #
    #     # return response


class HabitosCreateViewSet(CreateAPIView):
    queryset = Habito.objects.all()
    serializer_class = HabitosSerializer


    def perform_create(self, serializer):
        instance = serializer.save()

        # # Registra el cambio
        # mensaje = "Producto creado"
        # registrarCambio(self.request, instance, mensaje)
