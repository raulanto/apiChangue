from django.urls import path
from .routers import router
from .vista.pos_vista import PostCreateViewSet
from .vista.comentari_vista import ComentarioCreateViewSet
from .vista.trabajador_vista import TrabajadorCreateViewSet
from .vista.alimentacion_vista import AlimentacionCreateViewSet
from .vista.puntuacion_vista import PuntuacionCreateViewSet
from .vista.ejercicio_vista import EjercicioCreateViewSet
from .vista.habitos_vista import HabitosCreateViewSet
from .vista.rutina_vista import RutinaCreateViewSet

urlpatterns = [
    path('post/registro/', PostCreateViewSet.as_view(), name='postregistro'),
    path('comentario/registro/', ComentarioCreateViewSet.as_view(), name='comentarioregistro'),
    path('trabajador/registro/', TrabajadorCreateViewSet.as_view(), name='trabajadorregistro'),
    path('alimentacion/registro/', AlimentacionCreateViewSet.as_view(), name='alimentacionregistro'),
    path('puntuacion/registro/', PuntuacionCreateViewSet.as_view(), name='puntuacionnregistro'),
    path('ejercicio/registro/', EjercicioCreateViewSet.as_view(), name='ejernregistro'),
    path('habitos/registro/', HabitosCreateViewSet.as_view(), name='habitosnregistro'),
    path('rutina/registro/', RutinaCreateViewSet.as_view(), name='rurinanregistro'),
]

urlpatterns += router.urls
