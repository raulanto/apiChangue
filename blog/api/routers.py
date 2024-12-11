from rest_framework.routers import DefaultRouter
from .vista.pos_vista import PostViewSet
from .vista.comentari_vista import ComentarioViewSet
from .vista.trabajador_vista import TrabajadorViewSet
from .vista.puntuacion_vista import PuntuacionViewSet
from .vista.alimentacion_vista import AlimentacionViewSet
from .vista.etiquetas_vista import EtiquetaViewSet
from .vista.ejercicio_vista import EjercicioViewSet
from .vista.habitos_vista import HabitosViewSet
from .vista.rutina_vista import RutinaViewSet

router = DefaultRouter()
router.register(r'post', PostViewSet)
router.register(r'comentario', ComentarioViewSet)
router.register(r'trabajador', TrabajadorViewSet)
router.register(r'puntuacion', PuntuacionViewSet)
router.register(r'alimentacion', AlimentacionViewSet)
router.register(r'etiqueta', EtiquetaViewSet)
router.register(r'ejercicio', EjercicioViewSet)
router.register(r'habitos', HabitosViewSet)
router.register(r'rutina', RutinaViewSet)



