# Generated by Django 4.2.11 on 2024-03-15 03:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musicApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='liked_songs',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='playlists',
            field=models.CharField(max_length=255),
        ),
    ]
