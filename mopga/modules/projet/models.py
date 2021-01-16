from django.db import models
# Create your models here.


class Users(models.Model):
    name = models.CharField(max_length=200, unique=True)
    login = models.CharField(max_length=200, unique=True)
    password = models.CharField(max_length=200)
    karma = models.IntegerField(default=0)


class Projects(models.Model):
    title = models.CharField(max_length=200, unique=True)
    description = models.CharField(max_length=5000)
    copyright = models.CharField(max_length=200)
    score = models.IntegerField()
    beginDate = models.DateField(input_formats=['%d/%m/%Y'])
    deadline = models.DateField(input_formats=['%d/%m/%Y'])
    completed = models.BooleanField(default=False)
    donationGoal = models.IntegerField()


class Comments(models.Model):
    idProject = models.ForeingKey(Projects, on_delete=models.CASCADE)
    idUser = models.ForeingKey(Users, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=500)


class LeadBy(models.Model):
    idProject = models.ForeingKey(Projects, on_delete=models.CASCADE)
    idUser = models.ForeingKey(Users, on_delete=models.CASCADE)


class EvaluateBy(models.Model):
    idProject = models.ForeingKey(Projects, on_delete=models.CASCADE)
    idUser = models.ForeingKey(Users, on_delete=models.CASCADE)


class FundedBy(models.Model):
    idProject = models.ForeingKey(Projects, on_delete=models.CASCADE)
    idUser = models.ForeingKey(Projects, on_delete=models.CASCADE)

