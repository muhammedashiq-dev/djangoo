from django import forms 
from .models import customer_details

class customerform(forms.ModelForm):
    class Meta:
        model = customer_details
        fields = ['customer_name','email']
        