from django.db import models


class Component(models.Model):
    name = models.CharField(max_length=32)


class AccessHistory(models.Model):
    date_accessed = models.DateTimeField()
    rfid_used = models.CharField(max_length=32)
