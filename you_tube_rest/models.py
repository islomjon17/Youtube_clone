from django.db import models
from django.contrib.auth.models import User
# Create your models here.




class Video(models.Model):
    name = models.CharField(max_length=255)
    video_location = models.URLField()
    viewers = models.IntegerField()
    creation_time_video = models.DateTimeField(auto_now_add=True)
    GENDER_CHOICES = (
        ('P', 'popular'),
        ('U', 'unpopular'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)

class Comment(models.Model):
    video = models.ForeignKey(Video, blank=True, on_delete=models.CASCADE)
    description = models.CharField(max_length=500)

class MainUser(models.Model):
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    video = models.ForeignKey(Video, blank=True, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment,  blank=True, on_delete=models.CASCADE)

class Playlist(models.Model):
    title = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    creation_time_playlist = models.DateTimeField(auto_now_add=True)
    video = models.ManyToManyField(Video, blank=True)

