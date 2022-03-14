# Generated by Django 3.2.3 on 2022-03-14 09:26

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('psicologos', '0004_evaluacionpsicologico_psicologo'),
    ]

    operations = [
        migrations.AddField(
            model_name='evaluacionpsicologico',
            name='archivo2',
            field=models.FileField(blank=True, null=True, upload_to='evaluacionpsicologica/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf', 'png', 'jpeg', 'jpg'])]),
        ),
    ]