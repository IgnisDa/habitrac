from django.conf import settings
from django.db import models
from django.utils.translation import gettext as _


class Habit(models.Model):
    """An abstract model to track the habit cycle of a person for a certain duration.
    It is not meant to be used directly, but should be subclassed for various time
    durations"""

    name = models.CharField(
        max_length=200,
        help_text=_("The name of the particular habit you are trying to cultivate."),
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        help_text=_("The user that wants to cultivate this particular habit."),
    )
    started_on = models.DateTimeField(
        auto_now_add=True,
        help_text=_("The date and time this particular habit was started."),
    )
    duration = models.DurationField(
        help_text=_("The number of {0}s you plan to continue this habit for."),
    )
    progress = models.JSONField(
        help_text=_(
            "The progress of the habit being tracked. Each {0} (corresponding to "
            "duration) has a truth value whether that the habit was followed that "
            "{0} or not."
        ),
        blank=True,
        null=True,
    )

    class Meta:
        abstract = True
        constraints = [
            models.UniqueConstraint(
                fields=["user", "name"], name="unique_habit_name_for_%(class)s"
            )
        ]

    @classmethod
    def __get_help_text(cls, field):
        """ Returns the help_text for a single `field` """
        return str(cls._meta.get_field(field).help_text)

    @classmethod
    def get_all_help_text(cls, cycle_name):
        """ Returns the help_text for all the fields for this model """
        fields = cls._meta.fields
        return {
            field.name: cls.__get_help_text(field.name).format(cycle_name)
            for field in fields
            if field.name not in ["id", "progress"]
        }

    def tag_cycle(self, cycle_number):
        """ Marks the given `cycle_number` as done """
        self.progress[f"cycle-{cycle_number}"] = True

    def untag_cycle(self, cycle_number):
        """ Marks the given `cycle_number` as done """
        self.progress[f"cycle-{cycle_number}"] = False


class DailyHabit(Habit):
    def save(self, *args, **kwargs):
        if not self.pk:
            self.progress = {
                f"cycle-{cycle_number}": False
                for cycle_number in range(1, self.duration.days + 1)
            }
        return super().save(*args, **kwargs)

    @classmethod
    def get_all_help_text(cls):
        return super(DailyHabit, cls).get_all_help_text("day")

    def __str__(self):
        return f"{self.user} daily habit of {self.name}"


class HourlyHabit(Habit):
    def save(self, *args, **kwargs):
        if not self.pk:
            self.progress = {
                f"cycle-{cycle_number}": False
                for cycle_number in range(
                    1, int(self.duration.total_seconds() / 3600) + 1
                )
            }
        return super().save(*args, **kwargs)

    @classmethod
    def get_all_help_text(cls):
        return super(HourlyHabit, cls).get_all_help_text("hour")

    def __str__(self):
        return f"{self.user} hourly habit of {self.name}"
