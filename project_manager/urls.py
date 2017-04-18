from django.conf.urls import url, include
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
from rest_framework.urlpatterns import format_suffix_patterns
from django.views.static import serve

from django.conf import settings
from django.conf.urls.static import static

from project_manager import views
from project_manager.views import UserList, UserDetail, GroupList, GroupDetail

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^category/(?P<cat>.+)/$', views.category, name="category"),

    url(r'^api/$', views.api_root),
    url(r'^api/users/$', UserList.as_view(queryset=User.objects.all()), name='user-list'),
    url(r'^api/users/(?P<pk>\d+)/$', UserDetail.as_view(queryset=User.objects.all()),
        name='user-detail'),
    url(r'^api/groups/$', GroupList.as_view(queryset=Group.objects.all()), name='group-list'),
    url(r'^api/groups/(?P<pk>\d+)/$', GroupDetail.as_view(queryset=Group.objects.all()),
        name='group-detail'),
    url(r'^movie/(?P<id>\d+)/$', login_required(views.movie), name="movie"),
    url(r'^person/(?P<id>\d+)/$', views.person, name="person"),
]

# Format suffixes
urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json', 'api'])

# Default login/logout views
urlpatterns += [
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

# Default media
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
