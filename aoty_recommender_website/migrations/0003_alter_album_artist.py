# Generated by Django 5.0.7 on 2024-08-12 10:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aoty_recommender_website', '0002_album_artist_song'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='artist',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aoty_recommender_website.artist'),
        ),
    ]
