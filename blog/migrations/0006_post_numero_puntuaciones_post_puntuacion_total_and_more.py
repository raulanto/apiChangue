# Generated by Django 5.1.3 on 2024-12-05 04:12

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_trabajador'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='numero_puntuaciones',
            field=models.PositiveIntegerField(default=0, verbose_name='Número de puntuaciones'),
        ),
        migrations.AddField(
            model_name='post',
            name='puntuacion_total',
            field=models.PositiveIntegerField(default=0, verbose_name='Puntuación total'),
        ),
        migrations.CreateModel(
            name='Puntuacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('puntuacion', models.PositiveIntegerField(verbose_name='Puntuación')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='puntuaciones', to='blog.post', verbose_name='Post')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuario')),
            ],
            options={
                'verbose_name': 'Puntuación',
                'verbose_name_plural': 'Puntuaciones',
                'unique_together': {('post', 'usuario')},
            },
        ),
    ]