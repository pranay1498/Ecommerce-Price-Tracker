from django.db import models

# Create your models here.
from PriceTracker.scheduler import scheduler


class Amazon(models.Model):
    URL = models.URLField(max_length=10000)
    desired_price = models.FloatField()
    email = models.EmailField()
    time = models.DateTimeField()


class Flipkart(models.Model):
    URL = models.URLField(max_length=10000)
    desired_price = models.FloatField()
    email = models.EmailField()
    time = models.DateTimeField()


class Ebay(models.Model):
    URL = models.URLField(max_length=10000)
    desired_price = models.FloatField()
    email = models.EmailField()
    time = models.DateTimeField()


