from django.db import models
from .users import User


class Subject(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name
