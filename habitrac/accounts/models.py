import uuid
from typing import List

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _

from . import managers


def create_username_slug(username):
    """This is a function that returns a unique random slug taking into
    account whether a user with the generated slug already exists in the db."""
    return_val = None
    slug = slugify(username)
    while True:
        if not CustomUser.objects.filter(username_slug=slug).exists():
            return_val = slug
            break
        else:
            slug = slugify(username) + str(uuid.uuid4().hex.upper()[:6])
    return return_val


class CustomUser(AbstractUser):
    username = models.CharField(
        max_length=150, help_text=_("The username of the user."), unique=True
    )
    email = None
    username_slug = models.SlugField(
        max_length=100,
        help_text=_("The unique slug that will be used to identify the user"),
        editable=False,
    )

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS: List[str] = []

    objects = managers.CustomUserManager()

    class Meta:
        ordering = ("id",)

    def save(self, *args, **kwargs):
        if not self.pk:
            self.username_slug = create_username_slug(self.username)
        super(CustomUser, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.username}'s account"

    def get_report(self):
        number_of_habits = self.dailyhabit_set.count()
        completed_habits = len(
            [habit for habit in self.dailyhabit_set.all() if habit.is_completed]
        )
        done_habits = len(
            [habit for habit in self.dailyhabit_set.all() if habit.is_done]
        )
        return {
            "number_of_habits": number_of_habits,
            "completed_habits": completed_habits,
            "done_habits": done_habits,
        }
