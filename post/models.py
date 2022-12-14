from re import U
from turtle import title
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    author=models.ForeignKey(User, on_delete=models.CASCADE)
    title=models.CharField(max_length=120)
    content=models.TextField(max_length=500, blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title




        