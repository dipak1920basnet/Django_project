from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
import datetime

def index(request):
    now = datetime.datetime.now()

    if now.month == 1 and now.day == 1:
        new_year = True
    else:
        new_year = False

    return render(request, "newyear/index.html", {
        "newyear":new_year
        # "newyear":now.month == 1 and now.day == 1
    })
