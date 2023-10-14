from django.db import models
from .subject import Subject
from django.conf import settings


class Mark(models.Model):

    class Meta:
        unique_together = ('student', 'subject')

    mark = models.PositiveIntegerField()
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.student.first_name} - {self.subject.name}"

