from django.db import models
from .users import User


class Subject(models.Model):
    name = models.CharField(max_length=10)
    teacher = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
