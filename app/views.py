from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import permissions, generics


from django.http import HttpResponse, Http404

from app.models import Song, Record, Playlist
from app.serializers import SongSerializer, RecordSerializer, PlaylistSerializer
from app.permissions import IsOwnerOrReadOnly

class PlaylistList(generics.ListCreateAPIView):
    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PlaylistDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


class RecordList(generics.ListCreateAPIView):
    queryset = Record.objects.all()
    serializer_class = RecordSerializer
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class RecordDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Record.objects.all()
    serializer_class = RecordSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


class SongList(generics.ListCreateAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class SongDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]






