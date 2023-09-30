from django.db import models
from django.contrib.auth.models import Group, Permission


class UserMixin(models.Model):
    class Meta:
        abstract = True

    # first_name = models.CharField(max_length=200)
    # last_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200, unique=True, db_index=True)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)
    # groups = models.ManyToManyField(Group, related_name='custom_user_set')
    # user_permissions = models.ManyToManyField(Permission, related_name='custom_user_set')
