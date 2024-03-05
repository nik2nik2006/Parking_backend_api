from django.contrib.auth.hashers import make_password
from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager


class CustomUserManager(UserManager):
    # def __init__(self):
    #     self.name = None
    #     self._password = None
    #     self.password = None

    def _create_user(
            self,
            username: str,
            password: str,
            commit: bool,
            is_staff: bool = False,
            is_superuser: bool = False
    ):
        user = User(username=username, is_staff=is_staff, is_superuser=is_superuser)
        user.set_password(password)
        if commit:
            user.save()
        return user

    def create_superuser(self, username: str, password: str, commit: bool = True, first_name=None, otp=None):
        return self._create_user(username, password, first_name, otp, is_staff=True, is_superuser=True, commit=commit)

    def create_user(self, username: str, password: str, commit: bool = True, first_name=None, otp=None):
        return self._create_user(username, password, first_name, otp, commit=commit)

    # def set_password(self, raw_password):
    #     self.password = make_password(raw_password)
    #     self._password = raw_password


class User(AbstractUser):
    otp = models.PositiveIntegerField(blank=True, null=True)
    REQUIRED_FIELDS = []
    objects = CustomUserManager()
