from django.shortcuts import render
from django.http import HttpResponse
from django.core.serializers import serialize

from .models import Forecast
import json
import csv
import datetime
import time

import dateutil.parser
from .utils import date_formatter
# Create your views here.
def index(request):
    return HttpResponse(json.dumps({'msg':'Hello world'}), content_type="application/json")
    #return render(request, "index.html")



def seed(request):
    # dt = datetime.datetime(2016, 2, 25, 23, 23)    
    # myDate = time.mktime(dt.timetuple()) 
    # greeting = Forecast(lon=-180.0,lat=-90.0,forecast_time=dt,temperature=26.3,precipitation=8.8)
    # greeting.save()
    # greetings = Forecast.objects.all()
    # jsonSerialize = serialize('json', greetings)
    # # filenames = ["C:\Users\DELL\python-getting-started\\forecast\\file1.csv"]
    # # for fn in filenames:
    with open("forecast\\file1.csv") as f:
         
        reader = csv.reader(f , delimiter=',')
        line_count = 0
        for row in reader:
            print(row[2])
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
            # return HttpResponse(json.dumps({
            #     'lon' : row[0],
            #     'lat' : row[1],
            #     'forecast_time' : row[2],
            #     'temperature' : row[3] ,
            #     'precipitation' : row[4] 
            # }))    
            new_forecast.save()
    return HttpResponse("done")

