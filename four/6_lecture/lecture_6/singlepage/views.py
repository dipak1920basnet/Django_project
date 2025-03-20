from django.shortcuts import render
from django.http import Http404, HttpResponse
from django.http import JsonResponse
import time
# Create your views here.

def index(request):
    return render(request,"singlepage/index.html")

texts = ["Lorem ipsum dolor sit amet consectetur adipisicing elit. Corporis doloribus blanditiis ipsa. Quasi excepturi quibusdam aspernatur beatae veniam quas totam reprehenderit ratione, perspiciatis, repellat animi, culpa explicabo rem fugit qui?",
         "Lorem ipsum dolor sit, amet consectetur adipisicing elit. Nostrum, fugit praesentium! Suscipit dicta veritatis labore quas sint natus et accusantium? Adipisci quia deserunt nisi dolore maxime ipsum ad dignissimos delectus?",
         "Lorem ipsum dolor sit, amet consectetur adipisicing elit. Tenetur maxime, tempore nisi provident adipisci eaque nam ipsam recusandae ipsa doloribus error, eum itaque unde cupiditate eos nostrum culpa animi perferendis?"]

def section(request, num):
    if 1 <= num <=3:
        return HttpResponse(texts[num-1])
    
    else:
        raise Http404("No such section")
    

def scroll(request):
    return render(request, "singlepage/scroll.html")
    

