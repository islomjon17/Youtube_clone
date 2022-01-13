
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *
# router = DefaultRouter()
# router.register('video',PostViewSet)




urlpatterns = [
    # path('',include(router.urls)),
    path("videolist/", VideoGenricsView.as_view(), name='postlist'),
    path("commentlist/", CommentGenricsView.as_view(), name='postlist'),
    path("userlist/", UsersGenricsView.as_view(), name='postlist'),
    path("playlist/", PlayListGenricsView.as_view(), name='postlist'),
]

