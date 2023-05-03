from django.urls import path

from . import views

urlpatterns = [
    path('get-playlist-tracks/<str:id>', views.get_playlist_tracks, name="get_playlist_tracks"),
    path('search-playlist/<str:query>', views.search_playlist, name="search_playlist"),
    path('get-track-preview/<str:id>', views.track_preview, name="get_track_preview"),
    path('create-session/', views.create_session, name="create_session"),
]
