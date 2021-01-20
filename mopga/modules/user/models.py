from django.db import models
from django.contrib.auth.models import AbstractUser

#on a laissé la possibilité de donner plusieur point de karma a un utilisateur car cela simplifie les test
# mais si l'on voulait veritablement bloquer le karma++ nous simplement ajouté une liste de 'user' qui ont votées pour ce dit 'user'
class User(AbstractUser):
    karma = models.IntegerField(default=0)
    role = models.IntegerField()
    description = models.TextField(max_length=200)
    #voterKarma = models.ManyToManyField(User) #puis ajouter un if ou une exeption pour empecher le double voterKarma

    def is_maker(self):
        return self.role == 1

    def is_funder(self):
        return self.role == 2 or self.role == 3

    def is_rater(self):
        return self.role == 3 or self.role == 2

    def __str__(self):
        return self.username
