# Generated by Django 5.1.3 on 2024-12-05 02:16

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_remove_post_slug'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Trabajador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('telefono', models.CharField(blank=True, max_length=15, null=True, verbose_name='Teléfono')),
                ('ciudad', models.CharField(max_length=100, verbose_name='Ciudad')),
                ('edad', models.PositiveIntegerField(verbose_name='Edad')),
                ('foto_cedula', models.ImageField(blank=True, null=True, upload_to='cedulas/', verbose_name='Foto de la Cédula')),
                ('estado_solicitud', models.CharField(choices=[('en_proceso', 'En Proceso'), ('autorizado', 'Autorizado'), ('rechazado', 'Rechazado')], default='en_proceso', max_length=20, verbose_name='Estado de la Solicitud')),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('fecha_actualizacion', models.DateTimeField(auto_now=True, verbose_name='Fecha de actualización')),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='trabajador', to=settings.AUTH_USER_MODEL, verbose_name='Usuario')),
            ],
            options={
                'verbose_name': 'Trabajador',
                'verbose_name_plural': 'Trabajadores',
                'ordering': ['-fecha_creacion'],
            },
        ),
    ]