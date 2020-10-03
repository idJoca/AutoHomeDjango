from django.db import models

# Create your models here.


class User(models.Model):
    UserId = models.IntegerField()
    Name = models.CharField(max_length=100)
    CPF = models.CharField(max_length=32)
    Rg = models.CharField(max_length=32)
    Email = models.CharField(max_length=64)
    Password = models.CharField(max_length=32)
    PasswordHint = models.CharField(max_length=32)


class Component(models.Model):
    ComponentId = models.IntegerField()
    Name = models.CharField(max_length=32)


class AccessHistory(models.Model):
    AccessId = models.IntegerField()
    DateAccessed = models.DateTimeField()
    RFIDUsed = models.CharField(max_length=32)
