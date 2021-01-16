from django.db import models


# Create your models here.

class Projects(models.Model):
    title = models.CharField(max_length=200, unique=True)
    description = models.CharField(max_length=5000)
    copyright = models.CharField(max_length=200)
    score = models.IntegerField()
    beginDate = models.DateTimeField(editable=False)
    deadline = models.DateTimeField(input_formats=['/%d/%m/%Y'])
    completed = models.BooleanField(default=False)
    donationGoal = models.IntegerField()
    donaters = models.ManyToManyField(Member)
    annoncer = models.ForeignKey(Member, on_delete=models.CASCADE, related_name='annoncer')

    def save(self, *args, **kwargs):
        if not self.id:
            self.beginDate = timezone.now()
        return super(Comment, self).save(*args, **kwargs)


class Comments(models.Model):
    idProject = models.ForeingKey(Projects, on_delete=models.CASCADE)
    idUser = models.ForeingKey(Users, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=500)
    beginDate = models.DateTimeField(editable=False)

    def save(self, *args, **kwargs):
        if not self.id:
            self.beginDate = timezone.now()
        return super(Comment, self).save(*args, **kwargs)


class LeadBy(models.Model):
    idProject = models.ForeingKey(Projects, on_delete=models.CASCADE)
    idUser = models.ForeingKey(Users, on_delete=models.CASCADE)


class EvaluateBy(models.Model):
    idProject = models.ForeingKey(Projects, on_delete=models.CASCADE)
    idUser = models.ForeingKey(Users, on_delete=models.CASCADE)


class FundedBy(models.Model):
    idProject = models.ForeingKey(Projects, on_delete=models.CASCADE)
    idUser = models.ForeingKey(Projects, on_delete=models.CASCADE)
