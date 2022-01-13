from django.db.models import fields
from rest_framework import serializers
from .import models
from rest_framework.exceptions import ValidationError

class VideoSerializer(serializers.ModelSerializer):
    class Meta: 
        model = models.Video
        fields = ('id', 'name', 'video_location','viewers','creation_time_video', 'gender')

class CommentSerializer():
    class Meta: 
        model = models.Comment
        fields = ('id', 'description', 'video',)


class MainUserSerializer():
    class Meta: 
        model = models.MainUser
        fields = ('id', 'name', 'last_name','location','user', 'video','comment')

class PlaylistSerilaizer():
    class Meta: 
        model = models.Playlist
        fields = ('id', 'title', 'user','creation_time_playlist','video')