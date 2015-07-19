# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agency',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('url', models.URLField()),
                ('timezone', models.CharField(max_length=32)),
                ('lang', models.CharField(max_length=3)),
                ('phone', models.CharField(max_length=32)),
                ('fare_url', models.URLField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Route',
            fields=[
                ('id', models.CharField(max_length=32, serialize=False, primary_key=True)),
                ('short_name', models.CharField(max_length=3)),
                ('long_name', models.CharField(max_length=124)),
                ('desc', models.CharField(max_length=512)),
                ('type', models.IntegerField()),
                ('color', models.CharField(max_length=6)),
                ('text_color', models.CharField(max_length=6)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.CharField(max_length=128, serialize=False, primary_key=True)),
                ('monday', models.BinaryField()),
                ('tuesday', models.BinaryField()),
                ('wednesday', models.BinaryField()),
                ('thursday', models.BinaryField()),
                ('friday', models.BinaryField()),
                ('saturday', models.BinaryField()),
                ('sunday', models.BinaryField()),
                ('start_date', models.CharField(max_length=8)),
                ('end_date', models.CharField(max_length=8)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ServiceDate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.CharField(max_length=8)),
                ('exception_type', models.CharField(max_length=8)),
                ('service', models.ForeignKey(to='route.Service')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Stop',
            fields=[
                ('id', models.CharField(max_length=128, serialize=False, primary_key=True)),
                ('code', models.CharField(max_length=256)),
                ('name', models.CharField(max_length=256)),
                ('desc', models.CharField(max_length=256)),
                ('lat', models.FloatField()),
                ('lon', models.FloatField()),
                ('location_type', models.CharField(max_length=128)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('id', models.CharField(max_length=128, serialize=False, primary_key=True)),
                ('head_sign', models.CharField(max_length=128)),
                ('direction', models.BinaryField()),
                ('block', models.IntegerField()),
                ('shape', models.CharField(max_length=64)),
                ('route', models.ForeignKey(related_name='trips', to='route.Route')),
                ('service', models.ForeignKey(related_name='trips', to='route.Service')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TripStop',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('stop_sequence', models.IntegerField()),
                ('pickup_type', models.IntegerField()),
                ('drop_off_type', models.IntegerField()),
                ('stop', models.ForeignKey(related_name='trips', to='route.Stop')),
                ('trip', models.ForeignKey(related_name='stops', to='route.Trip')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
