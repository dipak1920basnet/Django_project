from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.

# tasks = ["foo","bar","baz"]
def index(request):
    if "tasks" not in request.session:
        request.session["tasks"] = []
    return render(request, "task/index.html",
                  {
                      "tasks":request.session["tasks"]
                  })

class NewTaskForm(forms.Form):
    task = forms.CharField(label = "New Task")
    # another_task = forms.CharField(label="Hello_New")

def add(request):
    # Check if method is POST
    if request.method == "POST":
        # Take in the data the user submitted and save it as form
        form = NewTaskForm(request.POST)

        if form.is_valid():
            task = form.cleaned_data["task"]
            # tasks.append(task)
            request.session["tasks"] += [task]
            return HttpResponseRedirect(reverse("task:index"))
        else:
            return render(request, "task/add.html",
                          {
                              "form":form
                          })
    return render(request, "task/add.html",
                  {
                      "form":NewTaskForm()
                  })

