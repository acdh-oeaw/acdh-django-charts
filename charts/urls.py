from django.conf.urls import url
from . import views

app_name = 'charts'

urlpatterns = [
    url(r'^chartselector/$', views.ChartSelector.as_view(), name='chart_selector'),
    url(
        r'^chart/(?P<model_name>[\w\-]+)/(?P<property>[\w\-]+)/(?P<charttype>[\w\-]+)/$',
        views.DynChartView.as_view(), name='dynchart'
    ),
]
