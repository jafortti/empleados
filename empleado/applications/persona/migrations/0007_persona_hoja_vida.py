# Generated by Django 3.2 on 2021-05-01 20:58

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('persona', '0006_rename_empleado_persona'),
    ]

    operations = [
        migrations.AddField(
            model_name='persona',
            name='hoja_vida',
            field=ckeditor.fields.RichTextField(default='texto'),
            preserve_default=False,
        ),
    ]