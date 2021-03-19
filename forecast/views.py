from django.http import HttpResponse,JsonResponse
import pandas as pd


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
    
    filenames = ["file1.csv", "file2.csv", "file3.csv"]
    for fn in filenames:        
        url =f'https://github.com/avishsa/python-getting-started/raw/main/forecast/{fn}'
        c = pd.read_csv(url)
        for index, row in c.iterrows():
            insert_forecast(row['Longitude'],
                                row['Latitude'],
                                row['forecast_time'],
                                row['Temperature Celsius'],
                                row['Precipitation Rate mm/hr']
            )
    return HttpResponse("done")
    

