from django.db import models

# Create your models here.
class USDExchangeRate(models.Model):
    month = models.CharField(max_length=50)
    year = models.IntegerField()
    average = models.DecimalField(max_digits=10, decimal_places=2)
    high = models.DecimalField(max_digits=10, decimal_places=2)
    low = models.DecimalField(max_digits=10, decimal_places=2)
