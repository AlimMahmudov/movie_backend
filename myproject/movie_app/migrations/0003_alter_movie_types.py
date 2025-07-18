# Generated by Django 5.2.2 on 2025-06-09 17:37

import multiselectfield.db.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0002_rename_gere_name_genre_genre_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='types',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('144p', '144p'), ('360p', '360p'), ('480p', '480p'), ('720p', '720p'), ('1080p', '1080p')], max_length=25),
        ),
    ]
