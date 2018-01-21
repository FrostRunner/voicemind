"""voicemind URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth.views import login
from django.urls import include, path

# class AboutView(TemplateView):
#     template_name = "/others/about.html"


urlpatterns = [
    path(r'', include("movie_app.urls")),
    path(r'^snip/', include('snippets.urls')),
    path(r'^login/', login, name="login"),
    path(r'^admin/', admin.site.urls),
    # url(r'^goods/', include("page.urls")),
    # url(r'^about', AboutView.as_view(), name="about"),
]
