from django.shortcuts import render
from django.http import HttpResponse

from .models import Forecast
import json
import csv
from datetime import datetime
import dateutil.parser
from decimal import Decimal, DecimalException

# Create your views here.
def index(request):
    return HttpResponse(json.dumps({'msg':'Hello world'}), content_type="application/json")
    #return render(request, "index.html")



def seed(request):
    
    
    greeting = Forecast(-180.0,-90.0, Decimal("1615986179"),26.3,8.8)
    
    greeting.save()
    greetings = Forecast.objects.all()
    # filenames = ["C:\Users\DELL\python-getting-started\\forecast\\file1.csv"]
    # for fn in filenames:
    # with open("forecast\\file1.csv") as f:
         
        # reader = csv.reader(f , delimiter=',')
        # line_count = 0
        # for row in reader:
        #     print(row[2])
        #     if line_count == 0:            
        #         line_count += 1
        #         continue
        #     new_forecast = Forecast(
        #         lon = row[0],
        #         lat = row[1],
        #         forecast_time = date_formatter(row[2]),
        #         temperature = row[3] ,
        #         precipitation = row[4] 
        #         )
        #     # return HttpResponse(json.dumps({
        #     #     'lon' : row[0],
        #     #     'lat' : row[1],
        #     #     'forecast_time' : row[2],
        #     #     'temperature' : row[3] ,
        #     #     'precipitation' : row[4] 
        #     # }))    
        #     new_forecast.save()
    return HttpResponse(json.dumps({"greetings": greetings}))

