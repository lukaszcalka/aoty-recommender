from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect


def home_page(request):
    return render(request, "home.html", {"data": "data"})


def login_user(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Success")
            return redirect('home')
        else:
            messages.error(request, "Not Success")
    return render(request, "login.html", {})


def logout_user(request):
    pass
