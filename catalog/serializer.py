from rest_framework import serializers

from .models import MusicianPerformer, Album, Song, SongInAlbum


class MusicianPerformerSerializer(serializers.ModelSerializer):
    """Исполнитель"""

    class Meta:
        model = MusicianPerformer
        fields = ('id', 'name',)


class AlbumSerializer(serializers.ModelSerializer):
    """Альбом"""

    class Meta:
        model = Album
        fields = ('id', 'performer', 'year',)


class SongSerializer(serializers.ModelSerializer):
    """Песня"""

    class Meta:
        model = Song
        fields = ('id', 'name',)


class SongInAlbumSerializer(serializers.ModelSerializer):
    """Песня в альбоме"""

    song = SongSerializer()

    class Meta:
        model = SongInAlbum
        fields = ('id', 'song', 'album', 'serial_number')

    def create(self, validated_data):
        song_name = validated_data.pop('song').get('name')
        song, _ = Song.objects.get_or_create(name=song_name, defaults={'name': song_name})
        return SongInAlbum.objects.create(song=song, album=validated_data.pop('album'),
                                          serial_number=validated_data.pop('serial_number'))

    def update(self, instance, validated_data):
        song_name = validated_data.pop('song').get('name')
        song, _ = Song.objects.get_or_create(name=song_name, defaults={'name': song_name})

        instance.song = song
        instance.album = validated_data.pop('album')
        instance.serial_number = validated_data.pop('serial_number')
        instance.save()
        return instance
