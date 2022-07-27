from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from .models import Post


class PostSerialzier(serializers.ModelSerializer):

    class Meta:
        model=Post
        fields=('id', 'author', 'title', 'content', 'created_at',)