from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Post
from .serializers import PostSerialzier
from .permissions import *
# Create your views here.


class PostList(generics.ListCreateAPIView):

    queryset=Post.objects.all()
    serializer_class=PostSerialzier


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes=[IsAuthorOrReadOnly,]
    queryset=Post.objects.all()
    serializer_class=PostSerialzier