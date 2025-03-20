from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def index(request, name):
    # return HttpResponse()
    return render(request, "dipak/index.html",
                  {
                      "name": name.capitalize()
                  })
