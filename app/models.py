from django.db import models
from django.contrib.auth import get_user_model
from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter
from pygments import highlight

class Song(models.Model):

    owner = models.ForeignKey('auth.User', related_name='songs', on_delete=models.CASCADE)
    highlighted = models.TextField()

    upload_date = models.DateField()
    name = models.CharField(max_length=200)
    file_name = models.TextField()
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

class Album(models.Model):

    owner = models.ForeignKey('auth.User', related_name='albums', on_delete=models.CASCADE)
    highlighted = models.TextField()

    artist = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    release_date = models.DateField()
    num_stars = models.IntegerField()
    size = models.IntegerField()

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
    representation of the code snippet.
    """
    lexer = get_lexer_by_name(self.language)
    linenos = 'table' if self.linenos else False
    options = {'title': self.title} if self.title else {}
    formatter = HtmlFormatter(style=self.style, linenos=linenos,
                              full=True, **options)
    self.highlighted = highlight(self.code, lexer, formatter)
    super(Snippet, self).save(*args, **kwargs)


