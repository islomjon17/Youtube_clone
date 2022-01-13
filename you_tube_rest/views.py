from django.shortcuts import render
from .serializers import VideoSerializer,CommentSerializer,MainUserSerializer,PlaylistSerilaizer
from .models import *

from rest_framework import generics
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
# Create your views here.


class VideoGenricsView(generics.ListAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['id', 'name', 'creation_time_video']
    search_fields = ['id', '=name', 'creation_time_video']
    ordering_fields = ['id', 'gender', 'viewers']


class CommentGenricsView(generics.ListAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['id', 'video',]
    search_fields = ['id', '=video', ]
    ordering_fields = ['id', 'video',]


class UsersGenricsView(generics.ListAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ['id', '=name', ]


class PlayListGenricsView(generics.ListAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['id', 'title',]
    search_fields = ['id', '=title', ]
    ordering_fields = ['id', 'creation_time_playlist',]