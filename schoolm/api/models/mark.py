from django.db import models
from .users import User
from .subject import Subject


class Mark(models.Model):

    class Meta:

        unique_together = ('student', 'subject')

    mark = models.IntegerField()
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.student.username} - {self.subject.name}"

