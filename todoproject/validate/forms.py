from django import forms
from django.core.validators import validate_email
from django.core.exceptions import ValidationError


def not_gmail(value):
    if value.find('@gmail') != -1:
        raise ValidationError(
            '%(value)s not allowed',
            params={'value': value},
        )


class Loginform(forms.Form):
    email = forms.CharField(
        max_length=100,
        min_length=10,
        validators=[validate_email, not_gmail]
    )
    password = forms.CharField(
        max_length=10,
        min_length=6
    )
