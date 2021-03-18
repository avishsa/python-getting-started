from django.db import models

# Create your models here.
class Forecast(models.Model):
    lon = models.DecimalField(max_digits=5, decimal_places=2,verbose_name="lon")
    lat = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="lat")
    forecast_time = models.DateTimeField(verbose_name="forecast time")
    temperature = models.FloatField(max_digits=5, decimal_places=2,verbose_name="temperature") 
    precipitation = models.FloatField(max_digits=5, decimal_places=2, verbose_name="precipitation") 