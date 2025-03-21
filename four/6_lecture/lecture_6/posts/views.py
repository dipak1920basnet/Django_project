from django.shortcuts import render

# Create your views here.
import time
from django.http import JsonResponse
from django.shortcuts import render

def index(request):
    return render(request,"posts/index.html")

def posts(request):
    start = int(request.GET.get("start") or 0)
    end = int(request.GET.get("end") or (start + 9))

    ## Generate list of posts

    data = []
    for i in range(start, end + 1):
        data.append(f"Post #{i}")

    ## Artificially delay speed of response

    time.sleep(1)

    #Return list of posts
    return JsonResponse(
        {
            "posts":data
        }
    )