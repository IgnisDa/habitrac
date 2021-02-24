from django.contrib import admin

from . import models


@admin.register(models.HourlyHabit)
class HourlyHabitAdmin(admin.ModelAdmin):
    readonly_fields = ("name_slug",)


@admin.register(models.DailyHabit)
class DailyHabitAdmin(admin.ModelAdmin):
    readonly_fields = ("name_slug",)
