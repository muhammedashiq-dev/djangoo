from django import forms
from django.core.validators import EmailValidator

class RegistrationForm(forms.Form):
    full_name = forms.CharField(
        min_length=5,
        max_length=50,
        widget=forms.TextInput(attrs={'placeholder': 'Full Name'})
    )
    email = forms.EmailField(
        validators=[EmailValidator()],
        widget=forms.EmailInput(attrs={'placeholder': 'Email'})
    )
    password = forms.CharField(
        min_length=8,
        max_length=20,
        widget=forms.PasswordInput(attrs={'placeholder': 'Password'})
    )
