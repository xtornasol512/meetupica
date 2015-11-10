# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=255)),
                ('fecha', models.DateTimeField(null=True, blank=True)),
                ('descripcion', models.TextField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='LugarEvento',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=255)),
                ('ubicacion', models.CharField(max_length=255, null=True, blank=True)),
                ('latitud', models.FloatField(null=True, blank=True)),
                ('altitud', models.FloatField(null=True, blank=True)),
                ('calificacion', models.IntegerField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Taller',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=255)),
                ('descripcion', models.TextField(null=True, blank=True)),
                ('horario', models.TimeField(null=True, blank=True)),
                ('evento', models.ForeignKey(to='eventos.Evento')),
                ('ponente', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='evento',
            name='lugar_evento',
            field=models.ForeignKey(to='eventos.LugarEvento'),
        ),
    ]
