# Generated by Django 5.1.3 on 2024-12-04 18:31

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Etiqueta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, unique=True, verbose_name='Nombre de la etiqueta')),
            ],
            options={
                'verbose_name': 'Etiqueta',
                'verbose_name_plural': 'Etiquetas',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200, unique=True, verbose_name='Título')),
                ('contenido', models.TextField(verbose_name='Contenido')),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('fecha_actualizacion', models.DateTimeField(auto_now=True, verbose_name='Fecha de actualización')),
                ('publicado', models.BooleanField(default=False, verbose_name='Publicado')),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to=settings.AUTH_USER_MODEL, verbose_name='Autor')),
                ('etiquetas', models.ManyToManyField(blank=True, related_name='posts', to='blog.etiqueta', verbose_name='Etiquetas')),
            ],
            options={
                'verbose_name': 'Publicación',
                'verbose_name_plural': 'Publicaciones',
                'ordering': ['-fecha_creacion'],
            },
        ),
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto', models.TextField(verbose_name='Comentario')),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comentarios', to=settings.AUTH_USER_MODEL, verbose_name='Autor')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comentarios', to='blog.post', verbose_name='Publicación')),
            ],
            options={
                'verbose_name': 'Comentario',
                'verbose_name_plural': 'Comentarios',
                'ordering': ['-fecha_creacion'],
            },
        ),
    ]