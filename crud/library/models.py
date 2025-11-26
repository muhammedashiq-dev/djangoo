from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
import datetime

class librarydatabase(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    year = models.IntegerField(
        validators=[
            MinValueValidator(1900),
            MaxValueValidator(datetime.datetime.now().year)
        ]
    )