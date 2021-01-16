from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    karma = models.IntegerField(default=0)
    is_validator = models.BooleanField(default=False)
    description_perso = models.TextField(max_length=200)

    def __str__(self):
        return self.username
