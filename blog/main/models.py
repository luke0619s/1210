from django.db import models
from django.utils import timezone
from django.template.defaultfilters import default
class location(models.Model):
    id = models.CharField(max_length=200,primary_key=True)
    latitude = models.CharField(max_length=200)
    longitude = models.CharField(max_length=200)
    name = models.CharField(max_length=100)
    info = models.CharField(max_length=200)
    temperature = models.CharField(max_length=200)
    icon = models.URLField(max_length=200)
    year = models.CharField(max_length=30,default=30)
    month = models.CharField(max_length=30,default=20)
    week  = models.CharField(max_length=30,default=20)