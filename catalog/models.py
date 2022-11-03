from django.db import models


class MusicianPerformer(models.Model):

    class Meta:
        verbose_name = "Исполнитель"
        verbose_name_plural = "Исполнители"

    name = models.CharField("Название", max_length=255)

    def __str__(self):
        return self.name


class Album(models.Model):

    class Meta:
        verbose_name = "Альбом"
        verbose_name_plural = "Альбомы"

    performer = models.ForeignKey(MusicianPerformer, on_delete=models.CASCADE, verbose_name="Исполнитель")
    year = models.PositiveIntegerField("Год выпуска", default=2020)

    def __str__(self):
        return f"{self.performer.name}:{self.year}"


class Song(models.Model):

    class Meta:
        verbose_name = "Песня"
        verbose_name_plural = "Песни"

    name = models.CharField("Название", max_length=255)

    def __str__(self):
        return self.name


class SongInAlbum(models.Model):

    class Meta:
        verbose_name = "Песня в альбоме"
        verbose_name_plural = "Песни в альбомах"

    album = models.ForeignKey(Album, on_delete=models.CASCADE, verbose_name="Альбом")
    song = models.ForeignKey(Song, on_delete=models.CASCADE, verbose_name="Песня")
    serial_number = models.PositiveIntegerField("Порядковый номер в альбоме", default=0)

    def __str__(self):
        return str(self.serial_number)
