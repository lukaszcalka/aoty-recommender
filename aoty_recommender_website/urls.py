from django.urls import path

from aoty_recommender_website import views

urlpatterns = [
    path("", views.home_page, name="home"),
    path("logout/", views.logout_user),
    path("register/", views.register_user),
    path("song/<int:pk>/", views.SongDetailView.as_view(), name="song_details"),
    path("album/<int:pk>/", views.AlbumDetailView.as_view(), name="album_details"),
    path("artist/<int:pk>/", views.ArtistDetailView.as_view(), name="artist_details"),
]
