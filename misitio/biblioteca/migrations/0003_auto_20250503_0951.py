# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2025-05-03 14:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biblioteca', '0002_auto_20250502_1758'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='autor',
            options={'ordering': ['nombre'], 'verbose_name_plural': 'Autores'},
        ),
        migrations.AlterModelOptions(
            name='editor',
            options={'ordering': ['nombre'], 'verbose_name_plural': 'Editores'},
        ),
        migrations.AlterField(
            model_name='autor',
            name='email',
            field=models.EmailField(blank=True, max_length=254),
        ),
        migrations.AlterField(
            model_name='libro',
            name='fecha_publicacion',
            field=models.DateField(blank=True, null=True),
        ),
    ]
