from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.
tasks = ["foo","bar","baz"]
def index(request):
    return render(request, "tasks/index.html",
                  {
                      "tasks":tasks
                  })

def add(request):
    if request.method == "POST":
        task = request.POST.get("task")
        if task not in tasks:
            tasks.append(task)
            return HttpResponseRedirect(reverse("tasks:index"))
        


    return render(request, "tasks/add.html")