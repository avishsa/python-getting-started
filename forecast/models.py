from django.db import models

# Create your models here.
class Forecast(models.Model):
    lon = models.FloatField(verbose_name="lon")
    lat = models.FloatField(verbose_name="lat")
    forecast_time = models.DateTimeField(verbose_name="forecast time")
    temperature = models.FloatField(verbose_name="temperature") 
    precipitation = models.FloatField(verbose_name="precipitation") 