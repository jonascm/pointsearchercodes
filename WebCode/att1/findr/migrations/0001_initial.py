# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-05 19:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SearchParams',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('origin', models.CharField(choices=[('ATL', 'Atlanta ATL'), ('JFK', 'New York JFK'), ('LGA', 'New York LGA'), ('SFO', 'San Francisco SFO'), ('LAX', 'Los Angeles LAX'), ('MIA', 'Miami MIA'), ('FLL', 'Ft Lauderdale FLL'), ('MSY', 'New Orleans MSY'), ('BOS', 'Boston BOS'), ('ORD', 'Chicago ORD'), ('HOU', 'HOuston HOU'), ('SLC', 'Salt Lake City SLC'), ('CLT', 'Charlotte CLT'), ('SEA', 'Seattle SEA'), ('MSP', 'Minneapolis - St Paul MSP')], max_length=3)),
                ('destination', models.CharField(choices=[('Europe', 'Europe'), ('Asia', 'Asia'), ('North America', 'North America'), ('Central America', 'Central America'), ('South America', 'South America'), ('ATL', 'Atlanta ATL'), ('JFK', 'New York JFK'), ('LGA', 'New York LGA'), ('SFO', 'San Francisco SFO'), ('LAX', 'Los Angeles LAX'), ('MIA', 'Miami MIA'), ('FLL', 'Ft Lauderdale FLL'), ('MSY', 'New Orleans MSY'), ('BOS', 'Boston BOS'), ('ORD', 'Chicago ORD'), ('HOU', 'HOuston HOU'), ('SLC', 'Salt Lake City SLC'), ('CLT', 'Charlotte CLT'), ('SEA', 'Seattle SEA'), ('MSP', 'Minneapolis - St Paul MSP')], max_length=20)),
                ('depdate', models.DateField()),
                ('retdate', models.DateField()),
                ('flexdates', models.BooleanField()),
                ('ariline', models.CharField(choices=[('DAL', 'Delta Airlines'), ('AA', 'American Arilines')], max_length=3)),
                ('maxnummiles', models.IntegerField()),
            ],
        ),
    ]
