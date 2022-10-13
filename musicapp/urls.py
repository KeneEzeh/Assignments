from django.urls import path, include
from . import views
from rest_framework import routers
from .views import ArtisteViewSet, SongViewSet, LyricViewSet

router = routers.DefaultRouter()
router.register(r'artiste', ArtisteViewSet)
router.register(r'song', SongViewSet)
router.register(r'lyric', LyricViewSet)


urlpatterns = [
    path('',include(router.urls)),    
]