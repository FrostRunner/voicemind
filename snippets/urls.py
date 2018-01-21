from django.urls import path
from snippets import views

urlpatterns = [
    path(r'^snippets/$', views.snippet_list),
    path(r'^snippets/(?P<pk>[0-9]+)/$', views.snippet_detail),
]