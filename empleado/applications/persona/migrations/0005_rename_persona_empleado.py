# Generated by Django 3.2 on 2021-05-01 19:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('departamento', '0002_auto_20210501_1632'),
        ('persona', '0004_persona_avatar'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Persona',
            new_name='Empleado',
        ),
    ]