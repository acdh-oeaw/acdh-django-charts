from django.core.management.base import BaseCommand, CommandError

from charts.models import ChartType


class Command(BaseCommand):

    help = "Delete all ChartTyp objects"

    def handle(self, *args, **options):
        all = ChartType.objects.all()
        self.stdout.write("{} Chart Type objects will be deleted".format(all.count()))
        all.delete()
        self.stdout.write("All ChartType objects are gone")
