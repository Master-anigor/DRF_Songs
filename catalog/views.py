from rest_framework import viewsets

from .models import MusicianPerformer, Album, SongInAlbum
from .serializer import MusicianPerformerSerializer, AlbumSerializer, SongInAlbumSerializer


class MusicianPerformerView(viewsets.ModelViewSet):

    serializers = {
        'default': MusicianPerformerSerializer,
        'list': MusicianPerformerSerializer,
    }

    def get_serializer_class(self):
        return self.serializers.get(self.action, self.serializers['default'])

    def get_queryset(self):
        return MusicianPerformer.objects.all()


class AlbumView(viewsets.ModelViewSet):

    serializers = {
        'default': AlbumSerializer,
        'list': AlbumSerializer,
    }

    def get_serializer_class(self):
        return self.serializers.get(self.action, self.serializers['default'])

    def get_queryset(self):
        return Album.objects.all()


class SongInAlbumView(viewsets.ModelViewSet):

    serializers = {
        'default': SongInAlbumSerializer,
        'list': SongInAlbumSerializer,
    }

    def get_serializer_class(self):
        return self.serializers.get(self.action, self.serializers['default'])

    def get_queryset(self):
        return SongInAlbum.objects.all()