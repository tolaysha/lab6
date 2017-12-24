from django.db import models

# Create your models here.


class Education(models.Model):
    id_university = models.AutoField(primary_key=True)
    name_university = models.CharField(max_length=100)


class Subjects(models.Model):
    id_subject = models.AutoField(primary_key=True)
    name_subject = models.CharField(max_length=100)


class Regions(models.Model):
    id_region = models.AutoField(primary_key=True)
    name_region = models.CharField(max_length=100)


class Tutors(models.Model):
    id_tutor = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45)
    surname = models.CharField(max_length=45)
    patronymic = models.CharField(max_length=45)
    email = models.EmailField(max_length=254)
    tel = models.CharField(max_length=20)
    birth_date = models.DateField()
    date_tutoring_begin = models.DateField()
    address = models.CharField(max_length=100)
    region = models.ForeignKey(Regions, on_delete=models.CASCADE)
    edu = models.ManyToManyField(Education)
    subjects = models.ManyToManyField(Subjects)
