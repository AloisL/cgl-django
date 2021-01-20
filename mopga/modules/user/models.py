from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    karma = models.IntegerField(default=0)
    role = models.IntegerField()
    description = models.TextField(max_length=200)
    funds = models.IntegerField(default=0)

    def is_maker(self):
        return self.role == 1

    def is_funder(self):
        return self.role == 2 | self.role == 3

    def is_rater(self):
        return self.role == 3 | self.role == 2

    def add_funds(self, new_funds):
        self.funds += new_funds
        return self.funds

    def remove_funds(self, funds_removed):
        self.funds += funds_removed
        return self.funds

    def __str__(self):
        return self.username
