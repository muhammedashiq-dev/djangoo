from django import forms
from .models import librarydb

class libraryform(forms.ModelForm):
    class Meta:
        model = librarydb
        fields = ['book_title','author_name']