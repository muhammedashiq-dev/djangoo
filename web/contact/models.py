from django.db import models

class contactinfo(models.Model):
    full_name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    phone_number = models.IntegerField(max_length=10)
