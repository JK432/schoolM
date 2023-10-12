from django.db import models
from django.contrib.auth.models import Group, Permission


class UserMixin(models.Model):
    class Meta:
        abstract = True
    ROLES = (
        (1, 'STUDENT'),
        (2, 'TEACHER'),
    )
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    roles = models.IntegerField(choices=ROLES, null=True)
    email = models.EmailField(max_length=200, unique=True, db_index=True)
