# Generated by Django 5.1.3 on 2024-12-05 06:31

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_alter_ejercicio_autor_alter_habito_autor_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='SeguimientoComida',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dia', models.CharField(choices=[('lunes', 'Lunes'), ('martes', 'Martes'), ('miercoles', 'Miércoles'), ('jueves', 'Jueves'), ('viernes', 'Viernes'), ('sabado', 'Sábado'), ('domingo', 'Domingo')], max_length=10, verbose_name='Día de la semana')),
                ('completado', models.BooleanField(default=False, help_text='Indica si se consumió la comida según el plan.', verbose_name='Completado')),
                ('fecha', models.DateField(default=datetime.date.today, help_text='Fecha en la que se registró el seguimiento.', verbose_name='Fecha')),
                ('observaciones', models.TextField(blank=True, help_text='Notas adicionales sobre la comida.', null=True, verbose_name='Observaciones')),
                ('comida', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='seguimientos_comida', to='blog.alimentacion', verbose_name='Comida')),
            ],
            options={
                'verbose_name': 'Seguimiento de Comida',
                'verbose_name_plural': 'Seguimiento de Comidas',
                'ordering': ['fecha', 'dia'],
                'unique_together': {('comida', 'dia', 'fecha')},
            },
        ),
    ]