from django.db import models


# Create your models here.
class Students(models.Model):
    photo = models.ImageField()
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    date = models.CharField(max_length=20)
    father_name = models.CharField(max_length=60)
    mother_name = models.CharField(max_length=60)
    address = models.CharField(max_length=120)
    number = models.CharField(max_length=50, default='+998')
    passport_number = models.CharField(max_length=12)


class Teachers(models.Model):
    photo = models.ImageField()
    name = models.CharField(max_length=90)
    education = models.CharField(max_length=50)


class News(models.Model):
    photo = models.ImageField()
    title = models.CharField(max_length=30)
    text = models.CharField(max_length=600)
    date = models.DateTimeField()
    from_to = models.CharField(max_length=30)


class StudentsAchievement(models.Model):
    photo = models.ImageField()
    title = models.CharField(max_length=30)
    text = models.CharField(max_length=600)
    date = models.DateTimeField()


class InformationSchool(models.Model):
    title = models.CharField(max_length=60)
    grade = models.CharField(max_length=2)