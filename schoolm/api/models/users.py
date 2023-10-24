from django.contrib.auth.models import AbstractBaseUser
from ..mixins import UserMixin
from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):

    def create_user(self, email, password, is_superuser=False, **extra_fields):
        if not email:
            raise ValueError('Username must be set')
        user = self.model(email=email, **extra_fields)
        if is_superuser:
            user.is_superuser = True
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):

        extra_fields.setdefault('is_active', True)
        is_superuser = True
        return self.create_user(email, password, is_superuser, **extra_fields)


class User(AbstractBaseUser, UserMixin):

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'role']
    objects = UserManager()

    class Meta:
        app_label = 'api'
        db_table = "api_user"

    def __str__(self):
        return self.email
