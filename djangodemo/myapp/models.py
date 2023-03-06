from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=100)
    release_date = models.DateTimeField('Movie Release Date')
    movei_data = models.CharField(max_length=1000)

# Create your models here.
