from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import render

from project_manager.models import Person, Movie
from project_manager.forms import PosterForm



from django.contrib.auth.models import User, Group
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework.response import Response
from project_manager.serializers import UserSerializer, GroupSerializer

@api_view(['GET'])
def api_root(request, format=None):
    """
    The entry endpoint of our API.
    """
    return Response({
        'users': reverse('user-list', request=request),
        'groups': reverse('group-list', request=request),
    })

class UserList(generics.ListCreateAPIView):
    """
    API endpoint that represents a list of users.
    """
    model = User
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    API endpoint that represents a single user.
    """
    model = User
    serializer_class = UserSerializer

class GroupList(generics.ListCreateAPIView):
    """
    API endpoint that represents a list of groups.
    """
    model = Group
    serializer_class = GroupSerializer

class GroupDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    API endpoint that represents a single group.
    """
    model = Group
    serializer_class = GroupSerializer

cats = ["Drama", "Action", "Adventure", "Crime", "Drama", "Sci-Fi", "Thriller", "Romance",
        "War", "Mystery", "Horror", "Animation", "Comedy", "Family", "Fantasy", "History",
        "Biography", "Sport", "Musical", "Western", "Music", "Documentary", "Film-Noir"]


def index(request, cat=None):
    try:
        movies = Movie.objects.all().order_by("movie_title")
    except:
        raise Http404
    return render(request, "project_manager/dashboard.html", {"elements": movies,
                                                              "redirect_link": "movie",
                                                              "cats": sorted(cats),
                                                              })


def category(request, cat=None):
    try:
        movies = Movie.objects.all().filter(genres__contains=cat).order_by("movie_title")
    except:
        raise Http404
    return render(request, "project_manager/dashboard.html", {"elements": movies,
                                                              "redirect_link": "movie",
                                                              "cats": sorted(cats),
                                                              })

# @login_required
def movie(request, id):
    form = PosterForm()
    persons = Person.objects.filter(id=id)
    if id == None:
        movie = Movie.objects.first()
    else:
        movie = Movie.objects.get(pk=id)
    return render(request, "project_manager/moive.html", {"elements": persons,
                                                          "redirect_link": "person",
                                                          "movie": movie,
                                                          "cats": sorted(cats),
                                                          "form": form,
                                                          })


def person(request, id):
    try:
        page_num = request.GET["page"]
    except KeyError:
        page_num = 1
    try:
        person = Person.objects.get(pk=id)
    except Person.DoesNotExist:
        raise Http404
    return render(request, "project_manager/person.html", {"person": person, "pn": page_num})
