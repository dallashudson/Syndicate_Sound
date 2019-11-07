from django.db import models
from django.contrib.auth import get_user_model
from synsound.song import Song


class Song(models.Model):
    upload_date = models.DateField()
    name = models.CharField(max_length=200)
    file_name = models.TextField()
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

class Album(models.Model):
    artist = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    release_date = models.DateField()
    num_stars = models.IntegerField()
    size = models.IntegerField()

class Playlist(models.Model):
    artist = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    creation_date = models.DateField()
    num_stars = models.IntegerField()
    size = models.IntegerField()
