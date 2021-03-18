from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.core.serializers.json import DjangoJSONEncoder
from django.forms.models import model_to_dict
from django.db.models import Max,Min,Avg

from .models import Forecast
import json
import csv
import datetime
import time

from .utils import date_formatter


# Create your views here.
def index(request):
    return HttpResponse(json.dumps({'msg':'Hello world'}), content_type="application/json")

def data(request):
    lat = request.GET.get('lat')
    lon = request.GET.get('lon')
    fc_qs = Forecast.objects.filter(lon=lon,lat=lat).values("forecastTime", "Temperature","Precipitation")
    return JsonResponse(list(fc_qs),safe=False)
def summarize(request):
    lat = request.GET.get('lat')
    lon = request.GET.get('lon')
    fc_qs = Forecast.objects.filter(lon=lon,lat=lat)
    temp_max = fc_qs.aggregate(Max('Temperature'))["temperature__max"]
    temp_min = fc_qs.aggregate(Min('Temperature'))["temperature__min"]
    temp_avg = round(fc_qs.aggregate(Avg('Temperature'))["temperature__avg"],2)
    preci_max = fc_qs.aggregate(Max('Precipitation'))["precipitation__max"]
    preci_min = fc_qs.aggregate(Min('Precipitation'))["precipitation__min"]
    preci_avg = round(fc_qs.aggregate(Avg('Precipitation'))["precipitation__avg"],2)
    json_sum ={
        'max':{
            "Temperature":temp_max,
            "Precipitation":preci_max
        },
        'min':{
            "Temperature":temp_min,
            "Precipitation":preci_min
        },
        'avg' :{
            "Temperature":temp_avg,
            "Precipitation":preci_avg
        }
    }
    return JsonResponse(json_sum)
def seed(request):
    filenames = ["forecast\\file1.csv", "forecast\\file2.csv", "forecast\\file2.csv"]
    for fn in filenames:
        with open(fn) as f:            
            reader = csv.reader(f , delimiter=',')
            line_count = 0
            for row in reader:
                if line_count == 0:            
                    line_count += 1
                    continue
                new_forecast = Forecast(
                    lon = row[0],
                    lat = row[1],
                    forecastTime = date_formatter(row[2]),
                    Temperature = row[3] ,
                    Precipitation = row[4] 
                    ) 
                new_forecast.save()
    print("done")
    return HttpResponse("done")

