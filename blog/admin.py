from django.contrib import admin
from django.http import HttpResponse
from django.template import loader

from .models import *

import csv

def generar_csv_ejercicios(modeladmin, request, queryset):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="ejercicios.csv"'
    writer = csv.writer(response)

    # Escribir encabezados
    writer.writerow(['Nombre', 'Descripción', 'Duración', 'Repeticiones', 'Nivel de Dificultad', 'Grupo Muscular', 'Fecha de Creación'])

    # Escribir datos
    for ejercicio in queryset:
        writer.writerow([
            ejercicio.nombre,
            ejercicio.descripcion,
            ejercicio.duracion,
            ejercicio.repeticiones,
            ejercicio.get_nivel_dificultad_display(),
            ejercicio.get_grupo_muscular_display(),
            ejercicio.fecha_creacion,
        ])

    return response

generar_csv_ejercicios.short_description = "Exportar ejercicios seleccionados como CSV"

class EjercicioAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'duracion', 'repeticiones', 'nivel_dificultad', 'grupo_muscular', 'fecha_creacion')
    actions = [generar_csv_ejercicios]

admin.site.register(Ejercicio, EjercicioAdmin)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["titulo", "fecha_creacion"]
    list_filter = ["autor"]







admin.site.register(Etiqueta)
admin.site.register(Comentario)
admin.site.register(Trabajador)
admin.site.register(Puntuacion)
admin.site.register(Habito)
admin.site.register(SeguimientoEjercicio)
admin.site.register(Rutina)
admin.site.register(Alimentacion)
admin.site.register(SeguimientoComida)
admin.site.register(Consumidor)
admin.site.register(SeguimientoRutina)
admin.site.register(DiaSemana)
admin.site.register(Actividad)
# Register your models here.
