from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from users.managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    """
    Custom user model
    """
    username = models.CharField(unique=True, max_length=20, blank=False, null=True)
    email = models.EmailField(unique=True, blank=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    staff = models.BooleanField(default=True, null=True, blank=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    @property
    def is_staff(self):
        return self.staff

    def __str__(self):
        return f"{self.username}" or ''
