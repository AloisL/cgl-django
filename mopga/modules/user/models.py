from django.contrib.auth.models import AbstractUser
from django.db import models

#on a laissé la possibilité de donner plusieur point de karma a un utilisateur car cela simplifie les test
# mais si l'on voulait veritablement bloquer le karma++ nous simplement ajouté une liste de 'user' qui ont votées pour ce dit 'user'
class User(AbstractUser):
    karma = models.IntegerField(default=0)
    role = models.IntegerField()
    description = models.TextField(max_length=200)
    funds = models.IntegerField(default=0)
    #voterKarma = models.ManyToManyField(User) #puis ajouter un if ou une exeption pour empecher le double voterKarma

    def is_maker(self):
        return self.role == 1

    def is_funder(self):
        return self.role == 2 or self.role == 3

    def is_rater(self):
        return self.role == 3 or self.role == 2

    def add_funds(self, new_funds):
        self.funds += new_funds
        return self.funds

    def remove_funds(self, funds_removed):
        self.funds += funds_removed
        return self.funds

    def __str__(self):
        return self.username
