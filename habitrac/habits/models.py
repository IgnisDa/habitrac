import uuid
from datetime import date

from dateutil.rrule import DAILY, rrule
from django.conf import settings
from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext as _


def create_name_slug(name):
    """This is a function that returns a unique random slug taking into
    account whether a habit with the generated slug already exists in the db."""
    return_val = None
    slug = slugify(name)
    while True:
        if not DailyHabit.objects.filter(name_slug=slug).exists():
            return_val = slug
            break
        else:
            slug = slugify(name) + str(uuid.uuid4().hex.upper()[:6])
    return return_val


class DailyHabit(models.Model):
    """An model to track the daily habit cycle of a person for a certain
    duration."""

    name = models.CharField(
        max_length=200,
        help_text=_("The name of the particular habit you are trying to cultivate."),
    )
    name_slug = models.SlugField(
        max_length=100,
        help_text=_("The unique slug that will be used to identify the habit"),
        editable=False,
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        help_text=_("The user that wants to cultivate this particular habit."),
    )
    description = models.TextField(
        help_text=_("A brief description of what the habit is going to be about")
    )
    date_from = models.DateField(
        help_text=_("The date this particular habit was started."),
    )
    date_to = models.DateField(
        help_text=_("The date this particular habit is supposed to be completed."),
    )
    progress = models.JSONField(
        help_text=_(
            "The progress of the habit being tracked. Each `date` (corresponding to "
            "duration) has a truth value whether that the habit was followed that "
            "day or not."
        ),
        blank=True,
        null=True,
    )
    vault = models.BooleanField(
        default=False,
        help_text=_(
            "Whether the habit will be stored in the vault, that is, not "
            "appear in the normal habit lists."
        ),
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["user", "name"], name="unique_habit_name_for_%(class)s"
            )
        ]
        ordering = ("-date_from",)

    def __str__(self):
        return f"{self.user.username}'s habit of {self.name}"

    def save(self, *args, **kwargs):
        if not self.pk:
            self.name_slug = create_name_slug(self.name)
        self.create_cycles()
        super(DailyHabit, self).save(*args, **kwargs)

    @classmethod
    def __get_help_text(cls, field):
        """ Returns the help_text for a single `field` """
        return str(cls._meta.get_field(field).help_text)

    def create_cycles(self):
        if not self.progress and not self.pk:
            self.progress = {
                dt.strftime("%Y-%m-%d"): False
                for dt in rrule(DAILY, dtstart=self.date_from, until=self.date_to)
            }
        else:
            trues = [key for key, value in self.progress.items() if value]
            self.progress = {
                dt.strftime("%Y-%m-%d"): dt.strftime("%Y-%m-%d") in trues
                for dt in rrule(DAILY, dtstart=self.date_from, until=self.date_to)
            }

    @classmethod
    def get_all_help_text(cls):
        """ Returns the help_text for all the fields for this model """
        fields = cls._meta.fields
        return {
            field.name: cls.__get_help_text(field.name)
            for field in fields
            if field.name not in ["id", "progress"]
        }

    def toggle_day(self, date):
        """ Toggles the given `date` as done or not """
        self.progress[date] = not self.progress[date]

    @property
    def is_completed(self):
        """ Boolean to indicate if all the cycles were completed """
        return all(self.progress.values())

    @property
    def is_done(self):
        """ Boolean to indicate whether the habit's end date has passed """
        return date.today() >= self.date_to

    def generate_report(self):
        total = len(self.progress)
        complete = len([value for value in self.progress.values() if value])
        incomplete = total - complete
        completion_percentage = round((complete / total) * 100, 2)
        return {
            "complete": complete,
            "date_to": self.date_to,
            "incomplete": incomplete,
            "total": total,
            "completion_percentage": completion_percentage,
        }
