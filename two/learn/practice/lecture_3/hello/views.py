from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("<h1 style=\"color:blue\">Hello, world!</h1>")

def template_index(request):
    return HttpResponse("<h1 style=\"color:red\">Hello, world!</h1>")