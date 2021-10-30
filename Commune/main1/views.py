from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import HttpResponse, HttpResponseRedirect, render
from django.urls import reverse
from django.db import connection
from .models import User, Follower
from django.db import IntegrityError
import datetime
from django.http import JsonResponse
import itertools


# Create your views here.


def index(request):
    return render(request, 'index.html')


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        email = request.POST["email"]
        password = request.POST["password"]
        user = authenticate(request, username=email, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "login.html", {
                "message": "Invalid email and/or password."
            })
    elif not request.user.is_authenticated:
        return render(request, "login.html")
    return HttpResponseRedirect(reverse("index"))


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        email = request.POST["email"]
        fname = request.POST["fname"]
        lname = request.POST["lname"]
        date = request.POST["date"]
        username = lname + fname
        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.first_name = fname
            user.last_name = lname
            user.date = date
            user.save()
        except IntegrityError as e:
            print(e)
            return render(request, "register.html", {
                "message": "Email address already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("setup"))
    return render(request, "register.html")


def setup(request):
    print(datetime.datetime.now().replace(tzinfo=datetime.timezone.utc))
    print(request.user.date_joined)
    if request.user.is_authenticated and datetime.datetime.now().replace(tzinfo=datetime.timezone.utc) - request.user.date_joined.replace(tzinfo=datetime.timezone.utc) < datetime.timedelta(days=10000):
        if request.method == "POST":
            username = request.POST.get("username")
            description = request.POST.get("description")
            user = request.user
            user.username = username
            user.description = description
            user.save()

    return HttpResponseRedirect(reverse("me"))


def profiles(request, name):
    person = User.objects.get(username=name)

    context = {
        "person": person,
        "followers": Follower.objects.filter(follower=person).count(),
        "following": Follower.objects.filter(following=person).count(),

    }
    return render(request, "profiles.html", context)


def me(request):
    person = User.objects.get(username=request.user)
    context = {
        "person": person,
        "followers": Follower.objects.filter(follower=person).count(),
        "following": Follower.objects.filter(following=person).count(),

    }
    return render(request, "profiles.html", context)


def search(request, context):

    result_username = User.objects.filter(
        username__contains=context)
    fname_username = User.objects.filter(
        first_name__contains=context)
    lname_username = User.objects.filter(
        last_name__contains=context)

    users = (result_username | fname_username | lname_username)
    users = set(users)
    print(list(users))
    print(lname_username)

    return JsonResponse([user.serialize() for user in list(users)], safe=False)


def post
