# Generated by Django 5.1.3 on 2024-12-05 06:04

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_seguimientoejercicio'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='seguimientoejercicio',
            name='autor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='seguimientoejercicio', to=settings.AUTH_USER_MODEL, verbose_name='Autor'),
        ),
    ]
