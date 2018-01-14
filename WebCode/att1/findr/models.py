# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.forms import ModelForm

ORIGIN_CHOICES = (
    ('ATL','Atlanta ATL'),
    ('JFK','New York JFK'),
    ('LGA','New York LGA'),
    ('SFO','San Francisco SFO'),
    ('LAX','Los Angeles LAX'),
    ('MIA','Miami MIA'),
    ('FLL','Ft Lauderdale FLL'),
    #('MSY','New Orleans MSY'),
    #('BOS','Boston BOS'),
    #('ORD','Chicago ORD'),
    #('HOU','HOuston HOU'),
    #('SLC','Salt Lake City SLC'),
    #('CLT','Charlotte CLT'),
    #('SEA','Seattle SEA'),
    #('MSP','Minneapolis - St Paul MSP'),
)

DESTINATN_CHOICES = (
    #('Europe','Europe'),
    #('Asia','Asia'),
    ('North America','North America'),
    #('Central America','Central America'),
    #('South America','South America'),
    ('ATL','Atlanta ATL'),
    ('JFK','New York JFK'),
    ('LGA','New York LGA'),
    ('SFO','San Francisco SFO'),
    ('LAX','Los Angeles LAX'),
    ('MIA','Miami MIA'),
    ('FLL','Ft Lauderdale FLL'),
    ('MSY','New Orleans MSY'),
    ('BOS','Boston BOS'),
    ('ORD','Chicago ORD'),
    ('HOU','HOuston HOU'),
    ('SLC','Salt Lake City SLC'),
    ('CLT','Charlotte CLT'),
    ('SEA','Seattle SEA'),
    ('MSP','Minneapolis - St Paul MSP'),
)

AIRLINE_CHOICES = (
    ('DAL', 'Delta Airlines'),
    ('AA', 'American Arilines'),
)

class SearchParams(models.Model):
    origin = models.CharField(max_length=3, choices=ORIGIN_CHOICES)
    destination = models.CharField(max_length=20, choices=DESTINATN_CHOICES)
    depdate = models.DateField(blank=False, null=False)
    retdate = models.DateField(blank=False, null=False)
    flexdates = models.NullBooleanField()
    ariline = models.CharField(max_length=3, choices=AIRLINE_CHOICES)
    maxnummiles = models.IntegerField()

    def __str__(self):              # __unicode__ on Python 2
        return self.name


class SearchParamsForm(ModelForm):
    class Meta:
        model = SearchParams
        fields = ['origin','destination','depdate','retdate','flexdates','ariline','maxnummiles']


