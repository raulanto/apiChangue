# Generated by Django 5.1.3 on 2024-12-05 01:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_comentario_options_alter_etiqueta_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='slug',
        ),
    ]