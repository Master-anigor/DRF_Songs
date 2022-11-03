# Generated by Django 4.1.2 on 2022-10-31 16:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.PositiveIntegerField(default=2020, verbose_name='Год выпуска')),
            ],
            options={
                'verbose_name': 'Альбом',
                'verbose_name_plural': 'Альбомы',
            },
        ),
        migrations.CreateModel(
            name='MusicianPerformer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Исполнитель',
                'verbose_name_plural': 'Исполнители',
            },
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Песня',
                'verbose_name_plural': 'Песни',
            },
        ),
        migrations.CreateModel(
            name='SongInAlbum',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serial_number', models.PositiveIntegerField(default=2020, verbose_name='Порядковый номер в альбоме')),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.album', verbose_name='Альбом')),
                ('song', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.song', verbose_name='Песня')),
            ],
            options={
                'verbose_name': 'Песня',
                'verbose_name_plural': 'Песни',
            },
        ),
        migrations.AddField(
            model_name='album',
            name='performer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.musicianperformer', verbose_name='Исполнитель'),
        ),
    ]
