# Generated by Django 5.1.3 on 2024-12-08 01:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0018_diasemana_actividad'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='publicado',
            field=models.BooleanField(verbose_name='Publicado'),
        ),
    ]