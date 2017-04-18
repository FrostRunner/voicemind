from django import forms
from project_manager.models import Movie

class PosterForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ["poster"]
