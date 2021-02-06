from django.contrib import admin

from . import models


@admin.register(models.HourlyHabit)
class HourlyHabitAdmin(admin.ModelAdmin):
    pass


@admin.register(models.DailyHabit)
class DailyHabitAdmin(admin.ModelAdmin):
    pass
