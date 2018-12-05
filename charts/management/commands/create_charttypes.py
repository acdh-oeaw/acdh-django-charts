from django.core.management.base import BaseCommand, CommandError

from charts.models import ChartType

CHART_TYPES = [
    ('bar', '<i class="fas fa-chart-bar"></i>'),
    ('pie', '<i class="fas fa-chart-pie"></i>'),
    ('line', '<i class="fas fa-chart-line"></i>'),
]


class Command(BaseCommand):

    help = "Populate database with basic char types"

    def handle(self, *args, **kwargs):
        all = ChartType.objects.all()
        self.stdout.write("{} Chart Type objects already existed".format(all.count()))
        for x in CHART_TYPES:
            ChartType.objects.get_or_create(
                name=x[0],
                icon=x[1]
            )
        self.stdout.write(
            "{} Chart Type objects exist now".format(ChartType.objects.all().count())
        )
