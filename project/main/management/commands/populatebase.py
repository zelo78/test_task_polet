from django.core.management.base import BaseCommand

from main.models import Vehicle
from main.factories import VehicleFactory


class Command(BaseCommand):
    help = "Populate DB with a few Vehicles for testing"

    def add_arguments(self, parser):
        parser.add_argument(
            "count",
            nargs="?",
            default=25,
            type=int,
            help="Count of Vehicles to be created, default 25",
        )

    def handle(self, *args, **options):
        count = options["count"]

        for model, model_factory, target_count in ((Vehicle, VehicleFactory, count),):
            current_count = model.objects.count()
            if current_count < target_count:
                model_factory.create_batch(target_count - current_count)
