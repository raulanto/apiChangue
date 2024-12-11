# Generated by Django 5.1.3 on 2024-12-05 18:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_consumidor'),
    ]

    operations = [
        migrations.CreateModel(
            name='RutinaGuardada',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('guardada_en', models.DateTimeField(auto_now_add=True, verbose_name='Guardada en')),
                ('consumidor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rutinas_guardadas', to='blog.consumidor', verbose_name='Consumidor')),
                ('rutina', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='guardada_por', to='blog.rutina', verbose_name='Rutina')),
            ],
            options={
                'verbose_name': 'Rutina Guardada',
                'verbose_name_plural': 'Rutinas Guardadas',
                'unique_together': {('consumidor', 'rutina')},
            },
        ),
    ]