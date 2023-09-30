from django.db import models
from .users import User


class Subject(models.Model):
    name=models.CharField(max_length=10)
    students = models.ManyToManyField(User, related_name='student_subjects')
    teachers = models.ManyToManyField(User, related_name='teacher_subjects')

    def __str__(self):
        return self.name
