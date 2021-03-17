from django.shortcuts import render
from django.http import HttpResponse

from .models import Greeting

# Create your views here.
def data(request):
    return HttpResponse(json.dumps({'data':1}), content_type="application/json")
    #return render(request, "index.html")



