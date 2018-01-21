from django.urls import path
from page import views

urlpatterns = [
    path(r'^(?:(?P<id>\d+)/)?$', views.index, name="index"),
    path(r'^good/(?P<id>\d+)/$', views.good, name="good"),
]
