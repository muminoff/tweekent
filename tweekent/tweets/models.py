from django.db import models


class User(models.Model):
    uid = models.CharField(max_length=255, primary_key=True)
    screen_name = models.CharField(max_length=255)
    geo_enabled = models.BooleanField(default=True)
    location = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    profile_image = models.URLField()
    timezone = models.CharField(max_length=255)
    created_at = models.DateTimeField()
    followers_count = models.PositiveIntegerField()


class Tweet(models.Model):
    text = models.CharField(max_length=160)
    user = models.ForeignKey('User')
    country_code = models.CharField(max_length=2)
    country = models.CharField(max_length=100)
