from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^(?P<account>[a-z]+)/(?P<num>[0-9]+)/', views.index, name='index'),
    url(r'^(?P<account>[a-z]+)/', views.index, name='index'),
]
