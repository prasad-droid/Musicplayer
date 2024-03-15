from django.db import models
# Create your models here.

class UserProfile(models.Model):
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    contact = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    liked_songs = models.CharField(max_length=255)
    playlists = models.CharField(max_length=255)

    def __str__(self):
        return self.username