from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from app import views

urlpatterns = [
    path('app/', views.PlaylistList.as_view()),
    path('app/<int:pk>/', views.PlaylistDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)