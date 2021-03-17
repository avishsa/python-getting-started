from django.shortcuts import render
from django.http import HttpResponse

from .models import Greeting
import json


# Create your views here.
def index(request):
    return HttpResponse(json.dumps({'msg':'Hello world'}), content_type="application/json")
    #return render(request, "index.html")


def db(request):
    greeting = Greeting()
    greeting.save()
    greetings = Greeting.objects.all()

    return render(request, "db.html", {"greetings": greetings})
