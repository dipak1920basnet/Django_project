from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, World")


def brian(request):
    return HttpResponse(f"Hello Brian")

def greet(request, name):
    return HttpResponse(f"Hello {name}")


## Working with the templates

def temp(request, name):
    # return HttpResponse(f"<h1 style=\'color:blue\'> Hello, world This is {name}!</h1>")
    return HttpResponse(f"<h1 style=\"color:blue\">Hello, world! This is {name}</h1>")

## Working with the rendring of templates

def main_one(request,name):
    return render(request, 'hello/index.html',
                  {
                      "name":name.capitalize()
                  })