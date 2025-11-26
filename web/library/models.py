from django.db import models

class librarydb(models.Model):
    book_title = models.CharField(max_length=100)
    author_name = models.CharField(max_length=100)
