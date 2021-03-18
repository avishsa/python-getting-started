from django.db import models

# Create your models here.
class Forecast(models.Model):
    lon = models.FloatField(verbose_name="lon")
    lat = models.FloatField(verbose_name="lat")
    forecastTime = models.DateTimeField(verbose_name="forecast time")
    Temperature = models.FloatField(verbose_name="temperature") 
    Precipitation = models.FloatField(verbose_name="precipitation") 