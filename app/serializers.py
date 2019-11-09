from rest_framework import serializers
from app.models import Song, Album, Playlist
class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ['id', 'name', 'file_name', 'user']

class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ['id', 'name', 'file_name', 'user']

class PlaylistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Playlist
        fields = ['id', 'artist', 'name', 'creation_date', 'num_stars', 'size']