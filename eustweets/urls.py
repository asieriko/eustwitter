from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^(?P<account>[a-z]+)/(?P<num>[0-9]+)/', views.results, name='results'),
    url(r'^(?P<account>[a-z]+)/', views.results, name='results'),
    url(r'^$', views.get_name, name='getname'),
]
