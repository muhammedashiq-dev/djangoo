from django import forms

class movieregistration(forms.Form):
    movie_name = forms.CharField(max_length=100)
    release_year = forms.IntegerField(min_value=1900,max_value=2025)