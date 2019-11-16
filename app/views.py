from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.http import HttpResponse, Http404

from app.models import Song, Album, Playlist
from app.serializers import SongSerializer, AlbumSerializer, PlaylistSerializer


def PlaylistList(generics.ListCreateAPIView):
    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer


def PlaylistDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer






