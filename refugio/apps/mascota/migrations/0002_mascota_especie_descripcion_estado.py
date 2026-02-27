# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mascota', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mascota',
            name='especie',
            field=models.CharField(
                choices=[
                    ('perro', 'Perro'),
                    ('gato', 'Gato'),
                    ('conejo', 'Conejo'),
                    ('ave', 'Ave'),
                    ('otro', 'Otro'),
                ],
                default='perro',
                max_length=20,
            ),
        ),
        migrations.AddField(
            model_name='mascota',
            name='descripcion',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='mascota',
            name='estado',
            field=models.CharField(
                choices=[
                    ('disponible', 'Disponible'),
                    ('en_proceso', 'En proceso de adopción'),
                    ('adoptado', 'Adoptado'),
                ],
                default='disponible',
                max_length=20,
            ),
        ),
        migrations.AlterField(
            model_name='mascota',
            name='sexo',
            field=models.CharField(
                choices=[
                    ('macho', 'Macho'),
                    ('hembra', 'Hembra'),
                ],
                default='macho',
                max_length=10,
            ),
        ),
    ]
