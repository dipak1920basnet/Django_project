from django.shortcuts import render
from django.http import JsonResponse
from .models import Task
from django.views.decorators.csrf import csrf_exempt
import json
# Create your views here.
def home(request):
    return render(request,"tasks/index.html")

def get_tasks(request):
    tasks = list(Task.objects.values())
    return JsonResponse({"tasks":tasks})

@csrf_exempt
def add_task(request):
    if request.method == "POST":
        data = json.loads(request.body) #Parse JSON request
        new_task = Task.objects.create(title=data["title"])
        return JsonResponse({"id":new_task.id, "title":new_task.title})
    
def delete_task(request, task_id):
    Task.objects.filter(id=task_id).delete()
    return JsonResponse({"message":"Task deleted"})


