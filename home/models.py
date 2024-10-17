from django.db import models
from django.utils import timezone


# Create your models here.

class Client(models.Model):
    Parent_name = models.CharField(max_length=30, null=True)
    email = models.EmailField(null=True)
    Child_name = models.CharField(max_length=30, null=True)
    Child_age = models.IntegerField(default=0)

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

    def __str__(self):
        return self.category
