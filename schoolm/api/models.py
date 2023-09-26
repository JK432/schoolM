from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Student(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Teacher(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Subject(models.Model):
    name=models.CharField(max_length=10)
    students =  models.ManyToManyField(Student)
    teachers =  models.ManyToManyField(Teacher)
    def __str__(self):
        return self.name

class Mark(models.Model):
    mark = models.IntegerField()
    student = models.OneToOneField(Student,on_delete=models.CASCADE)
    subject = models.OneToOneField(Subject,on_delete=models.CASCADE)



