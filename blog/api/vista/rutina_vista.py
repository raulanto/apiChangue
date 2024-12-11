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

from ...models.Rutina import Rutina
from ..serilizador.rutina_resi import RutinaSerializer


class RutinaViewSet(
    ListModelMixin,
    RetrieveModelMixin,
    DestroyModelMixin,
    UpdateModelMixin,
    GenericViewSet
):
    queryset =Rutina.objects.all()

    serializer_class = RutinaSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend,filters.SearchFilter]
    filterset_fields = ['nutriologo','id']

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


class RutinaCreateViewSet(CreateAPIView):
    queryset = Rutina.objects.all()
    serializer_class = RutinaSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        instance = serializer.save()

        # # Registra el cambio
        # mensaje = "Producto creado"
        # registrarCambio(self.request, instance, mensaje)
