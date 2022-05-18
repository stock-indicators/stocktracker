from turtle import update
from django.db import models

class Assets(models.Model):
    asset_name = models.TextField(max_length=30, null=False)
    shortcut = models.TextField(max_length=10, null=False)
    description = models.TextField(max_length=200, null=False)
    update = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.asset_name
