# Generated by Django 5.1.3 on 2024-12-05 06:27

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_seguimientoejercicio_autor'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='ejercicio',
            name='autor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ejercicioAutor', to=settings.AUTH_USER_MODEL, verbose_name='Autor'),
        ),
        migrations.AlterField(
            model_name='habito',
            name='autor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='habitosEjercicio', to=settings.AUTH_USER_MODEL, verbose_name='Autor'),
        ),
        migrations.CreateModel(
            name='Alimentacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_comida', models.CharField(help_text='Por ejemplo, Desayuno, Almuerzo, Cena, Merienda.', max_length=100, verbose_name='Nombre de la comida')),
                ('descripcion', models.TextField(blank=True, help_text='Detalles adicionales sobre esta comida o dieta.', null=True, verbose_name='Descripción')),
                ('horario', models.TimeField(help_text='Hora recomendada para consumir esta comida.', verbose_name='Horario')),
                ('calorias', models.PositiveIntegerField(help_text='Cantidad aproximada de calorías.', verbose_name='Calorías (kcal)')),
                ('proteinas', models.DecimalField(decimal_places=2, help_text='Gramos aproximados de proteínas.', max_digits=5, verbose_name='Proteínas (g)')),
                ('carbohidratos', models.DecimalField(decimal_places=2, help_text='Gramos aproximados de carbohidratos.', max_digits=5, verbose_name='Carbohidratos (g)')),
                ('grasas', models.DecimalField(decimal_places=2, help_text='Gramos aproximados de grasas.', max_digits=5, verbose_name='Grasas (g)')),
                ('nivel_importancia', models.CharField(choices=[('baja', 'Baja'), ('media', 'Media'), ('alta', 'Alta')], default='media', max_length=50, verbose_name='Nivel de importancia')),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('fecha_actualizacion', models.DateTimeField(auto_now=True, verbose_name='Fecha de actualización')),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='habitosautor', to=settings.AUTH_USER_MODEL, verbose_name='Autor')),
            ],
            options={
                'verbose_name': 'Alimentación',
                'verbose_name_plural': 'Alimentaciones',
                'ordering': ['horario'],
            },
        ),
        migrations.CreateModel(
            name='Rutina',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(help_text='Título descriptivo de la rutina.', max_length=255, verbose_name='Título')),
                ('descripcion', models.TextField(help_text='Detalles sobre la rutina y sus objetivos.', verbose_name='Descripción')),
                ('creado_en', models.DateTimeField(auto_now_add=True, verbose_name='Creado en')),
                ('actualizado_en', models.DateTimeField(auto_now=True, verbose_name='Actualizado en')),
                ('comidas', models.ManyToManyField(blank=True, related_name='rutinas', to='blog.alimentacion', verbose_name='Comidas')),
                ('ejercicios', models.ManyToManyField(blank=True, related_name='rutinas', to='blog.ejercicio', verbose_name='Ejercicios')),
                ('habitos', models.ManyToManyField(blank=True, related_name='rutinas', to='blog.habito', verbose_name='Hábitos')),
                ('nutriologo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rutinas', to='blog.trabajador', verbose_name='Nutriólogo')),
                ('post', models.OneToOneField(blank=True, help_text='Post donde se comparte esta rutina.', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='rutina', to='blog.post', verbose_name='Post asociado')),
            ],
            options={
                'verbose_name': 'Rutina',
                'verbose_name_plural': 'Rutinas',
                'ordering': ['creado_en'],
            },
        ),
    ]
