# Generated by Django 4.1.2 on 2022-10-13 11:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('musicapp', '0002_lyric_song_id_song_artiste_id_alter_song_likes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lyric',
            name='song_id',
        ),
        migrations.RemoveField(
            model_name='song',
            name='artiste_id',
        ),
    ]
