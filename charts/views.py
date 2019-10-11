import json

from collections import Counter

from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist, FieldError
from django.contrib.contenttypes.models import ContentType
from django.db.models import Count
from django.views.generic import TemplateView
from django.views.generic.list import ListView

from . models import ChartConfig

try:
    base_template = settings.CHARTS_BASE_TEMPLATE
except AttributeError:
    base_template = 'webpage/base.html'


class ChartSelector(ListView):
    model = ChartConfig
    template_name = 'charts/select_chart.html'

    def get_context_data(self, **kwargs):
        context = super(ChartSelector, self).get_context_data()
        context['base_template'] = base_template
        return context


def create_payload(model_name, property_name, charttype, qs, app_label=None):

    """ creates a dict which can be processed by highcharts"""

    context = {}
    payload = []
    objects = qs

    try:
        ct = ContentType.objects.get(
            app_label=app_label, model=model_name
        ).model_class()
        modelname = ct.__name__
    except ObjectDoesNotExist:
        context['fatal_error'] = True
        context['error_msg'] = "The model: <code>{}</code> you requested is not defined"\
            .format(model_name.title())
        return context

    try:
        chart = ChartConfig.objects.get(
            field_path=property_name,
            model_name=model_name,
            app_name=app_label
        )
        chart = chart.__dict__
    except ObjectDoesNotExist:
        context['error'] = True
        context['error_msg'] = """The ChartConfig Object:
            <code>field_path={}, model_name={}</code> you requested couldn't be found."""\
            .format(property_name, model_name.title())
        chart = {
            'legend_x': None,
            'legend_y': None,
            'label': 'not defined',
            'help_text': 'not defined'
        }
        if settings.DEBUG:
            pass
        else:
            context['fatal_error'] = True
# https://stackoverflow.com/questions/3432673/get-distinct-values-of-queryset-by-field
    try:
        values = qs.values(property_name)
        result = dict(Counter(
            [f"{x[property_name]}" for x in list(values)]
        ))
        try:
            result['Field not populated'] = result.pop(None)
        except KeyError:
            pass
        payload = [list(x) for x in list(result.items())]
        context['all'] = ct.objects.count()
        if chart['legend_x']:
            legendx = chart['legend_x']
        else:
            legendx = "# of {}s".format(modelname)
        data = {
            "items": "{} out of {}".format(objects.count(), context['all']),
            "title": "{}".format(chart['label']),
            "subtitle": "{}".format(chart["help_text"]),
            "legendy": chart["legend_y"],
            "legendx": legendx,
            "categories": "sorted(dates)",
            "measuredObject": "{}s".format(modelname),
            "ymin": 0,
            "payload": payload
        }
        context['data'] = data
    except FieldError:
        context['error'] = True
        context['error_msg'] = "The field: <code>{}</code> you requested does not exist"\
            .format(property_name)

    return context


class DynChartView(TemplateView):

    template_name = 'charts/dynchart.html'

    def get_context_data(self, **kwargs):
        context = super(DynChartView, self).get_context_data()
        context['base_template'] = base_template
        model_name = self.kwargs['model_name']
        property_name = self.kwargs['property']
        context['property_name'] = property_name
        context['charttype'] = self.kwargs['charttype']
        try:
            ct = ContentType.objects.get(model=model_name).model_class()
        except ObjectDoesNotExist:
            context['fatal_error'] = True
            context['error_msg'] = "The model: <code>{}</code> you requested is not defined"\
                .format(model_name.title())
            return context

        chartdata = create_payload(
            model_name,
            property_name,
            context['charttype'],
            ct.objects.all()
        )

        context = dict(context, **chartdata)

        return context
