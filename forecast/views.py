from django.http import HttpResponse,JsonResponse
import csv
import os
import urllib2

from .models import Forecast,Forecastsum
from .queries import get_data,get_sum,get_count
from .insertions import insert_forecast
from .validations import validLatAndLon

# Create your views here.
def index(request):
    return HttpResponse(json.dumps({'msg':'Hello world'}), content_type="application/json")
def count_data(request):
    return JsonResponse(get_count())
def data(request):
    lat = request.GET.get('lat')
    lon = request.GET.get('lon')
    err = validLatAndLon(lat,lon)
    if(err is not None):
        return JsonResponse(err)
    # return HttpResponse("vdss")
    return JsonResponse(get_data(lat,lon),safe=False)

def summarize(request):
    lat = request.GET.get('lat')
    lon = request.GET.get('lon')
    err = validLatAndLon(lat,lon)
    if(err is not None):
        return JsonResponse(err) 
    # return HttpResponse("vdss")   
    return JsonResponse(get_sum(lon,lat),safe=False)

def seed(request):
    module_dir = os.path.dirname(__file__)  # get current directory
#https://github.com/avishsa/python-getting-started/tree/main/forecast
    url_base= 'https://github.com/avishsa/python-getting-started/master/'    
    filenames = ["file1.csv", "file2.csv", "file2.csv"]
    
    for fn in filenames:
        response = urllib2.urlopen(url_base+fn)
        reader = csv.reader(response)
        line_count = 0
        for row in reader:
            if line_count == 0:
                line_count += 1                            
                continue            
            insert_forecast(row[0],row[1],row[2],row[3],row[4])
    return HttpResponse("done")

