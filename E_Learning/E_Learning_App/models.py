from django.db import models
from django.utils import timezone
# from embed_video.fields import EmbedVideoField


# Create your models here.

class Client(models.Model):
    Parent_name = models.CharField(max_length=30, null=True)
    password = models.CharField(max_length=30, null=True)
    email = models.CharField(max_length=30, null=True)
    Child_name = models.CharField(max_length=30, null=True)
    Child_age = models.IntegerField(default=0)
    message = models.CharField(max_length=250, null=True)
    objects = None

    def __str__(self):
        return self.Parent_name


class Cour(models.Model):
    CATEGORY = (
        ('Les Nombres', 'Les Nombres'),
        ('Alphabet', 'Alphabet'),
        ('Interactive', 'Interactive')
    )
    client = models.ForeignKey(Client, null=True, on_delete=models.SET_NULL)
    Date = models.DateTimeField(default=timezone.now)
    category = models.CharField(max_length=30, null=True, choices=CATEGORY)
    objects = None

    def __str__(self):
        return self.category

#
# class Video(models.Model):
#     title = models.CharField(max_length=100)
#     # url = EmbedVideoField(null=True)
#     VI_CAT = (
#         ('Les Nombres', 'Les Nombres'),
#         ('Alphabet', 'Alphabet'),
#         ('Interactive', 'Interactive')
#     )
#     Video_Category = models.CharField(max_length=30, null=True, choices=VI_CAT)
#     objects = None
#
#     def __str__(self):
#         return self.Video_Category
