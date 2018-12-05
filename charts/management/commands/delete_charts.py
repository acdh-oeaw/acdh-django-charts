from django.core.management.base import BaseCommand, CommandError

from charts.models import ChartConfig


class Command(BaseCommand):

    help = "Delete all ChartConfig objects"

    def handle(self, *args, **options):
        all = ChartConfig.objects.all()
        self.stdout.write("{} ChartConfig Type objects will be deleted".format(all.count()))
        all.delete()
        self.stdout.write("All ChartConfig objects are gone")
