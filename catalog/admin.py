from django.contrib import admin
from .models import MusicianPerformer, Album, Song, SongInAlbum


admin.site.register(MusicianPerformer)
admin.site.register(Album)
admin.site.register(Song)
admin.site.register(SongInAlbum)
