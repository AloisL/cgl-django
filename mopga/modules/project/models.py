from django.db import models
from django.utils import timezone

from mopga.modules.user.models import User


class Project(models.Model):
    title = models.CharField(max_length=200, unique=True)
    description = models.CharField(max_length=5000)
    copyright = models.CharField(max_length=200)
    beginDate = models.DateTimeField(editable=False)
    deadline = models.DateTimeField()
    completed = models.BooleanField(default=False)
    donationGoal = models.IntegerField(default=0)
    moneyCollected = models.IntegerField(default=0)
    imageName = models.CharField(max_length=200)
    donaters = models.ManyToManyField(User)
    annoncer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='annoncer')
    note = models.FloatField(default=0.0)

    def save(self, *args, **kwargs):
        if not self.id:
            self.beginDate = timezone.now()
        return super(Project, self).save(*args, **kwargs)

    def percentageFunded(self):
        percentage = self.moneyCollected / self.donationGoal * 100
        formatedPercentage = "{:.2f}".format(percentage)
        return formatedPercentage

    def setImageName(self, imageName):
        self.imageName = imageName
        self.save()

    def get_score(self):
        evaluations = EvaluateBy.objects.all()
        evaluations = evaluations.filter(idProject=self.id)
        if len(evaluations) == 0:
            return 0.0
        sum_notes = 0
        for e in evaluations:
            sum_notes += e.score
        return sum_notes / len(evaluations)

    def get_score_formatted(self):
        return "{:.2f}".format(self.get_score())


def setImagePath(instance, filename):
    return "mopga/static/data/projects/{}/images/{}".format(instance.projectId, filename)


class Image(models.Model):
    projectId = models.IntegerField()
    path = models.ImageField(upload_to=setImagePath)

    def save(self, *args, **kwargs):
        if not self.id:
            self.beginDate = timezone.now()
        return super(Image, self).save(*args, **kwargs)


class Comment(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=500)
    beginDate = models.DateTimeField(editable=False)

    def save(self, *args, **kwargs):
        if not self.id:
            self.beginDate = timezone.now()
        return super(Comment, self).save(*args, **kwargs)


class EvaluateBy(models.Model):
    idProject = models.ForeignKey(Project, on_delete=models.CASCADE)
    idUser = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.IntegerField(default=0)
