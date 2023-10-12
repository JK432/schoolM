from django.contrib.auth.models import AbstractBaseUser
from ..Mixins import UserMixin
from django.contrib.auth.models import UserManager


class User(AbstractBaseUser, UserMixin):

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']
    objects = UserManager()

    class Meta:
        app_label = 'api'
        db_table = "api_user"

    def __str__(self):
        return self.email
