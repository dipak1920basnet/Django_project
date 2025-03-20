from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, worlds!")

def brian(request):
    return HttpResponse("Hello Brain")

def david(request):
    return HttpResponse("Hello David!")
def template(request):
    return HttpResponse(f"<h1 style=\"color:blue\">Hello, Blue world!</h1>")
def greet(request, name):
    return HttpResponse(f"Hello {name.capitalize()}")



