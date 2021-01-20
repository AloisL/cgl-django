from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    karma = models.IntegerField(default=0)
    role = models.IntegerField()
    description = models.TextField(max_length=200)

    def is_maker(self):
        return self.role == 1

    def is_funder(self):
        return self.role == 2 | self.role == 3

    def is_rater(self):
        return self.role == 3 | self.role == 2

    def __str__(self):
        return self.username
