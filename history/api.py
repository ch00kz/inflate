from tastypie.resources import ModelResource
from history.models import USDExchangeRate


class USDExchangeRateResource(ModelResource):
    class Meta:
        queryset = USDExchangeRate.objects.all()
        resource_name = 'usd'
        allowed_methods = ['get']