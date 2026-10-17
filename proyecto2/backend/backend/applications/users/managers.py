from django.db import models
from django.contrib.auth.models import BaseUserManager

class UserManager(BaseUserManager):

    def _create_user(self, username, email, password, is_staff, is_superuser, **extra_fields):

        user = self.model(
            username = username,
            email = self.normalize_email(email=email),
            password = password,
            is_staff = is_staff,
            is_superuser = is_superuser,
            **extra_fields
        )

        user.set_password(password)

        user.save()

    def create_user(self, username, email, password, **extra_fields):

        return self._create_user(username, email, password, is_staff=False, is_superuser=False, **extra_fields)

    def create_superuser(self, username, email, password, **extra_fields):

        return self._create_user(username, email, password, is_staff=True, is_superuser=True, **extra_fields)