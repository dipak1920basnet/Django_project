from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

import datetime as dt

def index(request):
    time = dt.datetime.now()
    # if time.month == 1 and time.day==1:
    #     # return HttpResponse("Yes")
    #     return render(request, "newyear/index.html",
    #                   {
    #                       "name":"Yes"
    #                   })
    # else:
    #     # return HttpResponse("No")
    #     return render(request, "newyear/index.html",
    #                   {
    #                       "name":"No"
    #                   })

    return render(request, "newyear/index.html",
                  {
                      "NewYear": time.month == 1 and time.day==1
                  })