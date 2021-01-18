from django.db import models
from django.utils import timezone

from mopga.modules.user.models import User


class Projects(models.Model):
    title = models.CharField(max_length=200, unique=True)
    description = models.CharField(max_length=5000)
    copyright = models.CharField(max_length=200)
    score = models.IntegerField(default=0)
    beginDate = models.DateTimeField(editable=False)
    deadline = models.DateTimeField()
    completed = models.BooleanField(default=False)
    donationGoal = models.IntegerField(default=0)
    moneyCollected = models.IntegerField(default=0)
    donaters = models.ManyToManyField(User)
    annoncer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='annoncer')

    def save(self, *args, **kwargs):
        if not self.id:
            self.beginDate = timezone.now()
        return super(Projects, self).save(*args, **kwargs)

    def percentageFunded(self):
        return self.moneyCollected / self.donationGoal * 100


class Comments(models.Model):
    project = models.ForeignKey(Projects, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=500)
    beginDate = models.DateTimeField(editable=False)

    def save(self, *args, **kwargs):
        if not self.id:
            self.beginDate = timezone.now()
        return super(Comments, self).save(*args, **kwargs)


class EvaluateBy(models.Model):
    idProject = models.ForeignKey(Projects, on_delete=models.CASCADE)
    idUser = models.ForeignKey(User, on_delete=models.CASCADE)
