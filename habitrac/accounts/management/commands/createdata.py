from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
from django.utils.translation import gettext
from faker import Faker

CUSTOM_USER = get_user_model()


class Command(BaseCommand):

    help = gettext("Create instances of accounts.CustomUser. Defaults to 15.")

    def add_arguments(self, parser):
        parser.add_argument(
            "-i",
            "--instances",
            default=15,
            dest="instances",
            help=gettext("The number of data instances to be created."),
        )

    def handle(self, *args, **options):
        instances = int(options["instances"])
        fake = Faker()

        users = [
            CUSTOM_USER.objects.create_user(
                username=fake.user_name(), password=fake.password()
            )
            for _ in range(instances)
        ]

        self.stdout.write(self.style.SUCCESS(f"\nCreated {len(users)} users"))
