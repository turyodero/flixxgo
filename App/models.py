from django.db import models
from django.urls import reverse



class Movie(models.Model):
    HORROR = 'horror'
    ANIMATION= 'animation'
    SCIFI = 'scifi'
    ADULT = 'adult'
    ROMANCE = 'romance'
    ACTION = 'Action'
    COMEDY ='Comedy'
    ADVENTURE='Adventure'
    GENRE_CHOICES = [
        (HORROR, 'Horror'),
        (ADULT, 'Adult'),
        (ROMANCE, 'Romance'),
        (SCIFI , 'scifi'),
        (ANIMATION, 'animation'),
        (ACTION, 'Action'),
        (COMEDY, 'Comedy'),
        (ADVENTURE,'Adventure')
    ]

    title = models.CharField(max_length=255)
    coverphoto = models.ImageField(upload_to='movie_covers/')
    genre = models.CharField(max_length=10, choices=GENRE_CHOICES, default=HORROR)
    description = models.TextField()
    year = models.PositiveIntegerField()
    country= models.CharField(max_length=50)
    duration = models.TextField(max_length=10)
    link = models.URLField()


    class Meta:
        db_table = 'app_movie'

    def __str__(self):
        return self.title
    

class Serie(models.Model):
    HORROR = 'horror'
    ANIMATION= 'animation'
    SCIFI = 'scifi'
    ADULT = 'adult'
    DOCUMENTARY= 'documentary'
    ROMANCE = 'romance'
    ACTION = 'Action'
    COMEDY ='Comedy'
    ADVENTURE='Adventure'
    GENRE_CHOICES = [
        (HORROR, 'Horror'),
        (ADULT, 'Adult'),
        (ROMANCE, 'Romance'),
        (SCIFI , 'scifi'),
        (ANIMATION, 'animation'),
        (ACTION, 'Action'),
        (COMEDY, 'Comedy'),
        (ADVENTURE,'Adventure'),
        (DOCUMENTARY,'Documentary'),
    ]

    title = models.CharField(max_length=255)
    coverphoto = models.ImageField(upload_to='serie_covers/')
    genres = models.CharField(max_length=20, choices=GENRE_CHOICES, default=HORROR)
    description = models.TextField()
    year = models.PositiveIntegerField()
    country= models.CharField(max_length=50)
    duration = models.TextField(max_length=10)
    link = models.URLField()



    class Meta:
        db_table = 'app_serie'

    def __str__(self):
        return self.title
    

# Create your models here.
   