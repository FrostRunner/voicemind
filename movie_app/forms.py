from django import forms
from movie_app.models import Movie

class PosterForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ["poster"]
