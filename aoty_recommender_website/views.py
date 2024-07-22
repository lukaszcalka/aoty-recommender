from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

from aoty_recommender_website.forms import SignUpForm


def home_page(request):
    if request.method == "GET":
        return render(request, "home.html")
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
        else:
            messages.error(request, "We had a problem while logging you in")
        return render(request, "home.html")


def logout_user(request):
    pass


def register_user(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password1"]
            user = authenticate(email=email, password=password)
            login(request, user)
            return redirect("home")
    else:
        form = SignUpForm()
        return render(request, "register.html", {"form": form})

    return render(request, "register.html", {"form": form})
