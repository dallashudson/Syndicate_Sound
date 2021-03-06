from rest_framework import serializers
from app.models import Song, Record, Playlist
class SongSerializer(serializers.ModelSerializer):
    class Meta:
        owner = serializers.ReadOnlyField(source='owner.username')
        model = Song
        fields = ['id', 'name', 'file_name', 'user']

class RecordSerializer(serializers.ModelSerializer):
    class Meta:
        owner = serializers.ReadOnlyField(source='owner.username')
        model = Record
        fields = ['id', 'name', 'file_name', 'user']

class PlaylistSerializer(serializers.ModelSerializer):
    class Meta:
        owner = serializers.ReadOnlyField(source='owner.username')
        model = Playlist
        fields = ['id', 'artist', 'name', 'creation_date', 'num_stars', 'size']
