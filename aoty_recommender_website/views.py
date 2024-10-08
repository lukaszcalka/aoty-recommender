from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.views import generic

from aoty_recommender_website.forms import SignUpForm
from aoty_recommender_website.models import Album, Artist, Song
from aoty_recommender_website.scraper import AotyScraper


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


def search_albums(request, name):
    scraper = AotyScraper()
    img_srcs = scraper.search_albums(name)
    return render(request, "album_search.html", {"images_srcs": img_srcs})


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


class SongDetailView(generic.DetailView):
    model = Song
    template_name = "song_details.html"


class ArtistDetailView(generic.DetailView):
    model = Artist
    template_name = "artist_details.html"


class AlbumDetailView(generic.DetailView):
    model = Album
    template_name = "album_details.html"
