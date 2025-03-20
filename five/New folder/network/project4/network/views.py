from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse

from .models import User, Create_posting, Like, Followers
from django.contrib.auth.decorators import login_required
import json
from django.core.paginator import Paginator
from django.views.decorators.csrf import csrf_exempt

def index(request):

    post = Create_posting.objects.order_by("-timestamp").all()
    paginator = Paginator(post, 2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, "network/index.html",{
        "page_obj":page_obj,
        # "likes":,
    })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "network/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "network/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "network/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "network/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "network/register.html")

#Create a post
@login_required
def make_post(request):
    #Make a post
    if request.method != "POST":
        return JsonResponse({"error": "Need to give POST request"}, status=400)
    
    # data = json.load(request.body)
    # posts = [post.strip() for post in data.get("post").split(",")]
    # if posts ==[""]:
    #     return JsonResponse({"error": "There is nothing in post"}, status=400)
    # post = data.get("text",)
    post = request.POST["post"]
    posting = Create_posting.objects.create(post_creator=request.user, post=post)
    posting.save()

    return JsonResponse({
        "message":"Post created Successfully",
        "post_id": posting.id,
        "post": posting.post,
        "timestamp": posting.timestamp.strftime("%Y-%m-%d %H:%M:%S"),
        "post_creator": posting.post_creator.username
    }, status=201)
    # return HttpResponseRedirect('index')
    
    
## Viewing at other people's profile
def profile(request, id):
    try:
        user = User.objects.get(id=id)
    except User.DoesNotExist:
        return render(request, "network/profile.html",{"message":"User does not exist"})
    posts = Create_posting.objects.filter(post_creator=user).order_by("-timestamp")
    if posts.exists():
        paginator = Paginator(posts, 2)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
    else:
        return render(request, 'network/profile.html', {
        "message":"SOrry post don't exists",
        })
    return render(request, 'network/profile.html', {
        "page_obj":page_obj,
        "id":id,
        "follower_list":Followers.objects.filter(follower=id).all(),
    })

@login_required
def following(request):
    #Get the list of post
    posts = Create_posting.objects.order_by("-timestamp").all()
    show_post = []
    for post in posts:
        # Get all the name of the creator of the post
        m = Followers.objects.filter(user=post.post_creator)
        for follow in m:
            #Check if creator is followed by user
            if request.user == follow.follower:
                #Append the post of creator followed by user
                show_post.append(post)

    ## Working with pagination:
    paginator = Paginator(show_post,2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'network/following.html', {
        "page_obj":page_obj,
    })

#Follow and unfollow a user's profile
@login_required
@csrf_exempt
def follow(request, id):
    follower = request.user
    if request.method != "POST" :
        check = True
        try:
            user_to_follow = User.objects.get(id=id)
        except User.DoesNotExist:
            return JsonResponse({"error": "The user does not exists",
                             "check_action":check}, status=400)
        
        if_follow = Followers.objects.filter(id = id, user=user_to_follow, follower=follower)
        if not if_follow.exists():
            # if request.method == "GET":
                check = False
        return JsonResponse({"error": "GET or POST request required.",
                             "check_action":check}, status=400)
    
    data = json.loads(request.body)
    # data.get
    
    user_id = data.get("id")
    action = data.get("action")
    check = True
    try:
        user_to_follow = User.objects.get(id=id)
    except User.DoesNotExist:
        if request.method == "GET":
            check = False
        return JsonResponse({"message":"User does not exist.",
                            "check":check}, status=404)
    
    if request.method == "POST":
        if (action == "follow"):
            Followers.objects.create(id = user_id, user=user_to_follow, follower=follower)
        elif (action == "unfollow"):
            Followers.objects.filter(id = user_id, user=user_to_follow, follower=follower).delete()
        else:
            return JsonResponse({"message":"Action invalid"}, status=400)
    
    return JsonResponse({"message": "Data updated successfully"}, status=201)    
        
# Working with like and dislike
@login_required
@csrf_exempt
def like(request,id):
    liker = request.user
    if request.method == "POST":

        try:
            get_post_by_id = Create_posting.objects.get(id=id)
        except Create_posting.DoesNotExist:
            return JsonResponse({
            "message":"Liked or disliked on unavailable post"
        })
        else:
            get_post_by_liker = Like.objects.filter(liker=liker, on_post = get_post_by_id)
            if get_post_by_liker.exists():
                get_post_by_liker.delete()
                return JsonResponse({"message": "Like removed successfully"}, status=200)

            else:
                Like.objects.create(liker=liker, on_post = get_post_by_id) 
                return JsonResponse({"message": "Liked success"}, status=200)
 
        # except Like.DoesNotExist:

        # if liker not in post_likers:
    #         Like.objects.create(liker = liker, on_post = get_post_by_id)
    #     else:
    #         Like.objects.delete(liker = liker, on_post = get_post_by_id)
    #     return JsonResponse({
    #         "message":"Like updated successfullly",
    #     })
    else:
        try:
            get_post_by_id = Create_posting.objects.get(id=id)
        except Create_posting.DoesNotExist:
            return JsonResponse({"message":"The post does not exist"}, status=400)
        else:
            post_likers = Like.objects.filter(on_post = get_post_by_id).values_list('liker', flat=True)
            total_likes = len(list(post_likers))
            return JsonResponse({
                "total_likes":total_likes,
            })
    # # else:
    #     # try:
    #     #     get_post_by_id = Create_posting.objects.get(id=id)
    #     #     # post_likers = Like.objects.filter(on_post = get_post_by_id).values_list('liker', flat=True)   
    #     # except Like.DoesNotExist:

    #     # # if liker not in post_likers:
    #     #     Like.objects.create(liker = liker, on_post = get_post_by_id)
    #     # else:
    #     #     Like.objects.delete(liker = liker, on_post = get_post_by_id)
    #     # return JsonResponse({
    #     #     "message":"Like updated successfullly",
    #     # })
    #     # return JsonResponse({
    #     #     "message":"Responded"
        # })
            


    