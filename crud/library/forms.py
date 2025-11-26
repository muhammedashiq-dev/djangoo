from django import forms
from .models import librarydatabase

class libraryform(forms.ModelForm):
    class Meta:
        model = librarydatabase
        fields = ['title','author','year']