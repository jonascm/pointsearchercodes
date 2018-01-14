from django.conf.urls import url

from . import views

app_name = 'findr'
urlpatterns = [
    url(r'^$', views.searchform, name='searchform'),
    url(r'^results/$', views.results, name='results'),
]
