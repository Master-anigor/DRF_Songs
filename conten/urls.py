"""conten URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from .yasg import urlpatterns as doc_urls
from rest_framework import routers

from catalog import views
router = routers.DefaultRouter()
router.register(r'musician_performer', views.MusicianPerformerView, basename="musician_performer_api")
router.register(r'album', views.AlbumView, basename="album_api")
router.register(r'song_in_album', views.SongInAlbumView, basename="song_in_album_api")


urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),

]

urlpatterns += doc_urls