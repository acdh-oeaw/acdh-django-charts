from django import template
from django.contrib.contenttypes.models import ContentType
register = template.Library()


@register.inclusion_tag('charts/tags/load_highcharts_js.html', takes_context=True)
def load_highcharts_js(context):
    values = {}
    return values


@register.inclusion_tag('charts/tags/selector_dropdown.html', takes_context=True)
def selector_dropdown(context):
    return context


@register.inclusion_tag('charts/tags/config_highcharts.html', takes_context=True)
def config_highcharts(context):
    return context
