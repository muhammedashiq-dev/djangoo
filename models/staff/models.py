from django.db import models
from django.core.validators import validate_email

class customer_details(models.Model):
    customer_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100,validators=[validate_email])
    
