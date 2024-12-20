# Generated by Django 5.1.3 on 2024-12-05 06:02

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_habito'),
    ]

    operations = [
        migrations.CreateModel(
            name='SeguimientoEjercicio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dia', models.CharField(choices=[('lunes', 'Lunes'), ('martes', 'Martes'), ('miercoles', 'Miércoles'), ('jueves', 'Jueves'), ('viernes', 'Viernes'), ('sabado', 'Sábado'), ('domingo', 'Domingo')], max_length=10, verbose_name='Día de la semana')),
                ('completado', models.BooleanField(default=False, help_text='Indica si el ejercicio fue realizado.', verbose_name='Completado')),
                ('fecha', models.DateField(default=datetime.date.today, help_text='Fecha en la que se programó el ejercicio.', verbose_name='Fecha')),
                ('observaciones', models.TextField(blank=True, help_text='Notas adicionales sobre el ejercicio.', null=True, verbose_name='Observaciones')),
                ('ejercicio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='seguimientos', to='blog.ejercicio', verbose_name='Ejercicio')),
            ],
            options={
                'verbose_name': 'Seguimiento de Ejercicio',
                'verbose_name_plural': 'Seguimiento de Ejercicios',
                'ordering': ['fecha', 'dia'],
                'unique_together': {('ejercicio', 'dia', 'fecha')},
            },
        ),
    ]
