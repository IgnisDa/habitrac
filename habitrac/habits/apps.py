from django.apps import AppConfig
from django.conf import settings
from django.utils.autoreload import autoreload_started


def schema_watchdog(sender, **kwargs):
    sender.watch_file(settings.BASE_DIR, "**/*.graphql")


class HabitsConfig(AppConfig):
    name = "habits"

    def ready(self):
        autoreload_started.connect(schema_watchdog)
