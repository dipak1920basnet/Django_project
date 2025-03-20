from django.shortcuts import render
from django import forms
from django.urls import reverse
from django.http import HttpResponseRedirect
tasks = ["foo", "bar", "baz"]

# Create your views here.

def index(request):
    #Check if there already exists a "tasks" key in our session
    if "tasks" not in request.session:

        #If not, create a new list
        request.session["tasks"] = []

    return render(request, "new_total_task/new_index.html", {
        "tasks": request.session["tasks"]
    })

class NewTaskForm(forms.Form):
    task = forms.CharField(label="New Task")


def add(request):
    ## Check if method is POST:
    if request.method == "POST":
        form = NewTaskForm(request.POST)
        if form.is_valid():
            #Isolate the task from the 'cleaned' version of form data
            task = form.cleaned_data["task"]

            #Add the new task to our list of tasks
            tasks.append(task)

            #Redirectt user to list of tasks
            return HttpResponseRedirect(reverse("tasks:index"))
        
        else:
            #If the form is invalid, re-render the page with existing information.
            return render(request, "tasks/add.html",
                          {
                              "form":form
                          })

    return render(request,"new_total_task/add.html",
                  {
                      "form":NewTaskForm()
                  })

