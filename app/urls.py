from django.urls import path, include
from . import views

urlpatterns = [
    path('', include('app.urls'))
    path('app/', views.SizeOfPlist, name='Playlist Size'),
    path('app/', views.SizeOfAlbum, name='Album Size'),
]
