from django.db import models

# Create your models here.
class Users(models.Model):
    name = models.CharField(max_length=200, unique=True)
    identifiant = models.CharField(max_length=200, unique=True)
    motdepasse = models.CharField(max_length=200)
    karma = models.IntegerField(default=0)