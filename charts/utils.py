from django.apps import apps

from . models import ChartType, ChartConfig


def create_chart_config_obj(app_name, exclude_fields=[]):
    """
    Creates ChartConfig objects for all models defined in chosen app
    """
    exclude = exclude_fields
    try:
        models = [x for x in apps.get_app_config(app_name).get_models()]
    except LookupError:
        print("The app '{}' does not exist".format(app_name))
        return False

    barchart, _ = ChartType.objects.get_or_create(name='bar')

    for x in models:
        model_name = "{}".format(x.__name__.lower())
        print("Model: {}".format(model_name))
        for f in x._meta.get_fields(include_parents=False):
            if f.name not in exclude:
                field_name = f.name
                verbose_name = getattr(f, 'verbose_name', f.name)
                help_text = getattr(f, 'help_text', 'no helptext')
                print("{}: {} ({})".format(
                    model_name,
                    field_name,
                    help_text
                    )
                )
                chart_conf, _ = ChartConfig.objects.get_or_create(
                    model_name=model_name,
                    app_name=app_name,
                    field_path=field_name
                )
                chart_conf.chart_types.add(barchart)
                chart_conf.label = verbose_name
                chart_conf.help_text = help_text
                chart_conf.save()
            else:
                print("skipped: {}".format(f.name))
