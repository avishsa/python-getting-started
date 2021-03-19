from './models' import Forecast,Forecastsum
from './utils' import date_formatter
def insert_sumData(lon,lat,tMax,tMin,tAvg,pMax,pMin,pAvg):
    new_forecastsum = Forecastsum(
                    lon = lon,
                    lat = lat,
                    temp_max = tMax,
                    temp_min = tMin,
                    temp_avg = tAvg ,
                    Prec_max = pMax,
                    Prec_min = pMin ,
                    Prec_avg = pAvg ,
                    ) 
    new_forecastsum.save()
def insert_forecast(lon,lat,forecastTime,Temperature,Precipitation):
    new_forecast = Forecast(
                    lon = lon,
                    lat = lat,
                    forecastTime = date_formatter(forecastTime),
                    Temperature = Temperature ,
                    Precipitation = Precipitation 
                    ) 
    new_forecast.save()
    return new_forecast;