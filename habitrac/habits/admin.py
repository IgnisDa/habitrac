from django.contrib import admin

from . import models


@admin.register(models.DailyHabit)
class DailyHabitAdmin(admin.ModelAdmin):
    readonly_fields = (
        "name_slug",
        "progress",
    )
