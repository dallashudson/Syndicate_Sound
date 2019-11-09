from rest_framework import serializers
from apps.models import Song, Album, Playlist, LANGUAGE_CHOICES, STYLE_CHOICES

class MusicSerializer(serializers.Serializer):