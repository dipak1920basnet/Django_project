from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request,"hello/index.html")

def brian(request):
    return HttpResponse("Hello Brain")

def david(request):
    return HttpResponse("Hello, David")

def dipak(request):
    return HttpResponse("Hello Dipak Basnet")

def greet(request, name):
    # return HttpResponse(f"Hello {name.capitalize()}")
    return render(request, "hello/greet.html",{
        "name":name.capitalize()
    } ) 