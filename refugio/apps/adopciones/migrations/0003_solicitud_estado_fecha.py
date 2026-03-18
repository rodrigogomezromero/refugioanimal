# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adopciones', '0002_solicitud'),
    ]

    operations = [
        migrations.AddField(
            model_name='solicitud',
            name='estado',
            field=models.CharField(
                choices=[
                    ('pendiente', 'Pendiente'),
                    ('aprobada', 'Aprobada'),
                    ('rechazada', 'Rechazada'),
                ],
                default='pendiente',
                max_length=20,
            ),
        ),
        migrations.AddField(
            model_name='solicitud',
            name='fecha_solicitud',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
