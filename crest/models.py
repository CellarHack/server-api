from django.db import models

class Metric(models.Model):

    time = models.TimeField(auto_now=True)
    temp = models.FloatField()
    moist = models.FloatField()
    light = models.FloatField()

class Event(models.Model):

    time = models.TimeField(auto_now=True)
    event = models.CharField(max_length=32)
    value = models.IntegerField()
