from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.core.serializers.json import DjangoJSONEncoder
from django.forms.models import model_to_dict


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
    fc_qs = Forecast.objects.filter(lon=lon,lat=lat).values("forecast_time", "temperature","precipitation")
    return JsonResponse(list(fc_qs),safe=False)

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
                    forecast_time = date_formatter(row[2]),
                    temperature = row[3] ,
                    precipitation = row[4] 
                    ) 
                new_forecast.save()
    print("done")
    return HttpResponse("done")

