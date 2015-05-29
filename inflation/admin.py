from django.contrib import admin
from history.models import USDExchangeRate


@admin.register(USDExchangeRate)
class USDExchangeRate(admin.ModelAdmin):
    list_display = (
        'month', 'year', 'average', 'high', 'low'
    )