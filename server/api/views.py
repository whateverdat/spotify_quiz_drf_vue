from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
import time
from . import utils


# Create your views here.
@api_view(['GET'])
def search_playlist(request, query):
    '''
    Returns a single playlist:
        Name, Description, Spotify ID, Cover Art and Total Number of Tracks
    '''
    token = utils.get_token()
    result = utils.search_for_playlist(token, query)

    # Formatting Data
    data = {'name': result['name'], 'description': result['description'], 'spotifyID': result['id'], 'image': result['images'][0]['url'], 'songs': result['tracks']['total']}
    return Response(data)


@api_view(['GET'])
def get_playlist_tracks(request, id):
    '''
    Returns each song in a Playlist and for each song:
        Newly assigned ID, Spotify Track ID, Name, Album, and Cover Art
    '''
    token = utils.get_token()
    # result = utils.search_for_playlist(token, "This is Metallica") # Hardcoded
    # playlist_id = result["id"]
    songs = utils.get_playlist_tracks(token, id)

    # Formatting Data
    data = []
    diff = 1
    for idx, song in enumerate(songs):
        new = {}
        try:
            new['id'] = idx + diff
            new['spotifyID'] = song['track']['id']
            new['name'] = song['track']['name']
            new['album'] = song['track']['album']['name']
            new['image'] = song['track']['album']['images'][0]['url']
            new['preview_url'] = song['track']['preview_url']
        except TypeError:
            diff = diff -1
            pass
        else:
            data.append(new)

    return Response({'tracks': data})

# UNUSED
@api_view([''])
def track_preview(request, id):
    '''
    Returns 30sec Spotify Track audio preview when provided with spotify track id
    '''
    return None
    # token = utils.get_token()
    # track_data = utils.get_track_preview(token, id)
    # return Response({'preview_url': track_data})

# UNUSED
@api_view([])
def create_session(request):
    '''
    Sends session data
    '''
    return None
    # playlist_id = request.query_params["id"]
    # token = utils.get_token()
    # songs = utils.get_playlist_tracks(token, playlist_id)

    # session = []
    # for idx, song in enumerate(songs):
    #     track_id = song["track"]["id"]
    #     new = utils.get_track_preview(token, track_id)
    #     if new:
    #         session.append(new)

    # return Response({'session': session})
