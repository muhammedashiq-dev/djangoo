from django import forms

class contactform(forms.Form):
    full_name = forms.CharField(max_length=100,min_length=10)
    email = forms.EmailField(max_length=100)
    phone_number = forms.IntegerField(max_value=10)