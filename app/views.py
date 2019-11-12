from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponse

from app.models import Song, Album, Playlist
from app.serializers import SongSerializer, AlbumSerializer, PlaylistSerializer

#@api_view(['GET', 'POST'])  use to choose the function, need to further investigate

def index(request):
    return HttpResponse("Hello, world.")

def SizeOfPlist(request):
    return HttpResponse("The size of your playlist is ___ songs") #dummy function

def SizeOfAlbum(request):
    return HttpResponse("The size of the Album is ___ songs")

