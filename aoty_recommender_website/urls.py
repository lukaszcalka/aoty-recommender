from django.urls import path

from aoty_recommender_website import views

urlpatterns = [
    path("", views.home_page, name='home'),
    path("login/", views.login_user),
    path("logout/", views.logout_user)
]
