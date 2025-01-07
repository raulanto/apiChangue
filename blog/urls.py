from django.urls import path

from blog.views.ejercicio.view import (
    EjercicioListView,
    EjercicioCreateView,
    EjercicioDeleteView,
    EjercicioUpdateView,
    EjercicioDetailView,
)


app_name = 'blog'

urlpatterns = [
    path('ejercicio/', EjercicioListView.as_view(), name='ejercicio_list'),
    path('<int:pk>/', EjercicioDetailView.as_view(), name='ejercicio_detail'),
    path('create/', EjercicioCreateView.as_view(), name='ejercicio_create'),
    path('<int:pk>/update/', EjercicioUpdateView.as_view(), name='ejercicio_update'),
    path('<int:pk>/delete/', EjercicioDeleteView.as_view(), name='ejercicio_delete'),

]
