from django.urls import path

from aoty_recommender_website import views

urlpatterns = [
    path("home/", views.home_page)
]
