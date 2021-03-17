from django.db import models

# Create your models here.
class Forecast(models.Model):
    lon = models.DecimalField(max_digits=5, decimal_places=2)
    lat = models.DecimalField(max_digits=5, decimal_places=2)
    forecast_time = models.DateTimeField()
    temperature = models.DecimalField(max_digits=5, decimal_places=2) 
    precipitation = models.DecimalField(max_digits=5, decimal_places=2) 