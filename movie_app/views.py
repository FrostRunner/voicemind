from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import render

from movie_app.models import Person, Movie
from movie_app.forms import PosterForm

from django.core.paginator import Paginator, InvalidPage

from django.contrib.auth.models import User, Group
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework.response import Response
from movie_app.serializers import UserSerializer, GroupSerializer

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
        page_num = request.GET["page"]
    except KeyError:
        page_num = 1

    try:
        movies = Movie.objects.all().order_by("title_en")
    except:
        raise Http404

    pag = Paginator(movies, 20, orphans=5)

    try:
        movies = pag.page(page_num)
    except InvalidPage:
        movies = pag.page(1)


    return render(request, "movie_app/dashboard.html", {"elements": movies,
                                                              "redirect_link": "movie",
                                                              "cats": sorted(cats),
                                                              })


def category(request, cat=None):
    try:
        page_num = request.GET["page"]
    except KeyError:
        page_num = 1

    try:
        movies = Movie.objects.all().filter(genres__contains=cat).order_by("title_en")
    except:
        raise Http404

    # pag = Paginator(movies, 20, orphans=5)

    from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
    paginator = Paginator(movies, 20, orphans=5)
    page = request.GET.get('page')
    try:
        movies = paginator.page(page)
    except PageNotAnInteger:
        movies = paginator.page(1)
    except EmptyPage:
        movies = paginator.page(paginator.num_pages)

    return render(request, "movie_app/dashboard.html", {"elements": movies,
                                                              "redirect_link": "movie",
                                                              "cats": sorted(cats),
                                                              })

# @login_required
def movie(request, id):
    persons = Person.objects.filter(id=id)
    if id == None:
        movie = Movie.objects.first()
    else:
        movie = Movie.objects.get(pk=id)

    form = PosterForm(request.POST, request.FILES, instance=movie)
    if form.is_valid():
        form.save()

    return render(request, "movie_app/moive.html", {"elements": persons,
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
    return render(request, "movie_app/person.html", {"person": person, "pn": page_num})
