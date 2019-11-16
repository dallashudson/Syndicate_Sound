from django.db import models
from django.contrib.auth import get_user_model


class Song(models.Model):

    owner = models.ForeignKey('auth.User', related_name='songs', on_delete=models.CASCADE)
    highlighted = models.TextField()

    upload_date = models.DateField()
    name = models.CharField(max_length=200)
    file_name = models.TextField()
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        """
        Use the `pygments` library to create a highlighted HTML
        representation of the playlist.
        """
        upload_date = self.upload_date
        file_name = 'stars' if self.linenos else False #all bruh moments im not sure how we collect these
        options = {'title': self.name} if self.name else {}
        self.highlighted = highlight(self.name)
        super(Song, self).save(*args, **kwargs)

class Album(models.Model):

    owner = models.ForeignKey('auth.User', related_name='albums', on_delete=models.CASCADE)
    highlighted = models.TextField()

    artist = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    release_date = models.DateField()
    num_stars = models.IntegerField()
    size = models.IntegerField()

    def save(self, *args, **kwargs):
        """
        Use the `pygments` library to create a highlighted HTML
        representation of the playlist.
        """
        artist = self.artist
        num_stars = 'stars' if self.linenos else False #all bruh moments im not sure how we collect these
        options = {'title': self.name} if self.name else {}
        self.highlighted = highlight(self.name)
        super(Album, self).save(*args, **kwargs)

class Playlist(models.Model):

    owner = models.ForeignKey('auth.User', related_name='playlists', on_delete=models.CASCADE)
    highlighted = models.TextField()

    artist = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    creation_date = models.DateField()
    num_stars = models.IntegerField()
    size = models.IntegerField()

    def save(self, *args, **kwargs):
        """
        Use the `pygments` library to create a highlighted HTML
        representation of the playlist.
        """
        artist = self.artist
        num_stars = 'stars' if self.linenos else False #all bruh moments im not sure how we collect these
        options = {'title': self.name} if self.name else {}
        self.highlighted = highlight(self.name)
        super(Playlist, self).save(*args, **kwargs)


