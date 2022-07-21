from tkinter import CASCADE
from turtle import update
from django.db import models
from django.contrib.auth.models import User


class Topic(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Assets(models.Model):
    name = models.TextField(max_length=30, null=False)
    shortcut = models.TextField(max_length=10, null=False)
    description = models.TextField(max_length=200, null=False)
    update = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-update', '-created']

    def __str__(self):
        return self.name

 

class TwitterFollows(models.Model):
    name = models.TextField(max_length=50, null=False)
    link = models.URLField(max_length=128, unique=True, null=False)
    description = models.TextField(max_length=200, null=False)
    def __str__(self):
        return self.name

class Message(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    updated = models.DateField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.body[0:50]
