from django.contrib import admin
from .models import ChartType, ChartConfig


class ChartConfigAdmin(admin.ModelAdmin):
    list_display = ('model_name', 'app_name', 'label', 'field_path')
    list_filter = ('model_name', 'app_name')


admin.site.register(ChartConfig, ChartConfigAdmin)
admin.site.register(ChartType)
