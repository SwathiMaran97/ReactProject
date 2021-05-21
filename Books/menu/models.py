from django.db import models
from django.contrib.auth.models import User,Group
from django_pandas.managers import DataFrameManager
# Create your models here.
class menu(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True,null=True)
    updated = models.DateTimeField(auto_now=True,null=True)
