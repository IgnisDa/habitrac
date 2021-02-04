from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from . import managers


class CustomUser(AbstractUser):
    username = models.CharField(
        max_length=150, help_text=_("The username of the user."), unique=True
    )
    email = None

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = []

    objects = managers.CustomUserManager()

    class Meta:
        ordering = ("id",)

    def __str__(self):
        return f"{self.username}'s account"
