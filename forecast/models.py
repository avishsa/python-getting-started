from django.db import models

# Create your models here.
class Forecast(models.Model):
    lon = models.FloatField(verbose_name="lon")
    lat = models.FloatField(verbose_name="lat")
    forecastTime = models.DateTimeField(verbose_name="forecast time")
    Temperature = models.FloatField(verbose_name="temperature") 
    Precipitation = models.FloatField(verbose_name="precipitation") 

class Forecastsum(models.Model):
    lon = models.FloatField(verbose_name="lon")
    lat = models.FloatField(verbose_name="lat")
    temp_max = models.FloatField(verbose_name="temperature max")
    temp_min = models.FloatField(verbose_name="temperature min")
    temp_avg = models.FloatField(verbose_name="temperature avg")
    Prec_max = models.FloatField(verbose_name="precipitation max")
    Prec_min = models.FloatField(verbose_name="precipitation min")
    Prec_avg = models.FloatField(verbose_name="precipitation avg")