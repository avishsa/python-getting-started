from django.shortcuts import render
from django.http import HttpResponse

from .models import Forecast
import json
import csv
from .utils import date_formatter
# Create your views here.
def index(request):
    return HttpResponse(json.dumps({'msg':'Hello world'}), content_type="application/json")
    #return render(request, "index.html")



def seed(request):
    # filenames = ["C:\Users\DELL\python-getting-started\\forecast\\file1.csv"]
    # for fn in filenames:
    with open("forecast\\file1.csv") as f: 
        reader = csv.reader(f , delimiter=',')
        line_count = 0
        for row in reader:
            print(row[2])
            if line_count == 0:            
                line_count += 1
                continue
            new_forecast = Forecast.objects.get_or_create(
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
            forecast.save()
    return HttpResponse("seed successfully")

