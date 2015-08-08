from django.db import models


class User(models.Model):
    screen_name = models.CharField(max_length=255)
    location = models.CharField(max_length=100)
    description = models.CharField(max_length=255, null=True, blank=True)
    name = models.CharField(max_length=255)
    profile_image = models.URLField()


class Tweet(models.Model):
    text = models.CharField(max_length=160)
    timestamp = models.CharField(max_length=32)
    user = models.ForeignKey('User')
