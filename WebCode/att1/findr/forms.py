from django import forms

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

class SearchParamsForm(forms.Form):
    origin = forms.CharField(
        max_length=3,
        widget=forms.Select(choices=ORIGIN_CHOICES),
    )
    destination = forms.CharField(
        max_length=20,
        widget=forms.Select(choices=DESTINATN_CHOICES),
    )
    depdate = forms.DateField(required=True)
    retdate = forms.DateField(required=True)
    flexdates = forms.NullBooleanField()
    airline = forms.CharField(
        max_length=3,
        widget=forms.Select(choices=AIRLINE_CHOICES),
    )
    maxnumofmiles = forms.IntegerField(required=True)

