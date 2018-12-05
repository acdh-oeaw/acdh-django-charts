from django.core.management.base import BaseCommand, CommandError

from charts.utils import create_chart_config_obj


class Command(BaseCommand):

    help = "Create Chart objects for app"

    def add_arguments(self, parser):
        parser.add_argument(
            'app_name', type=str,
            help="Name of the app for which you'd like to create BrowsConf objects."
        )

    def handle(self, *args, **kwargs):
        app_name = kwargs['app_name']
        # exclude_fields = kwargs['exclude_fields']
        create_chart_config_obj(app_name)
