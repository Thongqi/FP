from django.contrib.auth import authenticate, login, logout
from django.core import serializers
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.forms import ModelForm, Textarea
from django.shortcuts import render, get_object_or_404
from django.urls import reverse


import json
from .models import User, Create


def index(request):
    if request.method == 'POST':
 
        data = request.body
        data = data.decode('utf-8')

        data = json.loads(data)
        data = data.get("addpost", "")
        newpost = Create(owner=request.user, post=data)
        newpost.save()
        post = list(Create.objects.filter(post=data, owner=request.user).order_by('-createdOn')[:1].values())
        # user = list(request.user.values())
        return JsonResponse({"post": post}, safe=False)
        # form = NewPostForm(request.POST)
        # if form.is_valid():
        #     newpost = form.save(commit=False)
        #     newpost.user = request.user
        #     form.save()
        
        # return HttpResponseRedirect(reverse("index"))

        
    elif request.method == 'POST' and 'like' in request.POST:
        post = get_object_or_404(Create, id=request.POST.get('like'))
        #if user already like, remove user from like
        if post.like.filter(id=request.user.id).exists():
            post.like.remove(request.user)
            liked = False
        else:
            post.like.add(request.user)
            liked = True
        return HttpResponseRedirect(reverse("index"))
    else:
        form = NewPostForm()
        posts = Create.objects.all().order_by('-createdOn')

        return render(request, "network/index.html", {
            "form": form,
            "posts":posts,

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

def profile(request, id):
    profile = User.objects.get(id=id)
    username = profile.username
    followers = profile.no_of_followers
    follow = profile.no_of_follows
    #posts from this user
    posts = Create.objects.filter(owner=id).order_by('-createdOn')
    
    #user's profile
    user = User.objects.get(username=request.user)
    
    if request.method == 'POST':
        #people's profile
        #status = request.body
        if user.followers.filter(username=username).exists():
            user.followers.remove(id)
            status = 'Follow'
        else:
            user.followers.add(id)
            status = 'Following'
        data = {'status': status}
        return JsonResponse(data, safe=False)
        
    else:
        if not user.followers.filter(username=username).exists():
            status = 'Follow'
        else:
            status = 'Following'
        return render(request, "network/profile.html", {
            "username":username,
            "followers": followers,
            "follow":follow,
            "posts": posts,
            "user": user,
            "status": status,
            "id":id,
        })


class NewPostForm(ModelForm):
    class Meta:
        model = Create
        fields = ["post"]
        widget = {
            "post": Textarea(attrs={"cols": 80,"rows":20, "id":"addpost"}),
        }
 

def get_all_posts(request):
    pass
    # posts = list(Create.objects.order_by('-createdOn').values())

    # return JsonResponse({"posts": posts}, safe=False)