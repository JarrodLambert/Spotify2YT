import spotipy
from spotipy.oauth2 import SpotifyOAuth
from ytmusicapi import YTMusic
import time

def get_spotify_playlist_tracks(sp, playlist_id):
    tracks = []
    offset = 0
    while True:
        response = sp.playlist_items(
            playlist_id,
            offset=offset,
            fields='items.track.name,items.track.artists(name),items.track.id,total',
            additional_types=['track']
        )
        if not response['items']:
            break
        tracks.extend(response['items'])
        offset += len(response['items'])
    return tracks

def main():
    # Replace these with your Spotify app credentials
    SPOTIFY_CLIENT_ID = 'you_spotify_client_id'
    SPOTIFY_CLIENT_SECRET = 'you_spotify_client_secret'
    SPOTIFY_REDIRECT_URI = 'http://localhost:8888/callback'

    # Replace with your Spotify playlist ID
    SPOTIFY_PLAYLIST_ID = 'you_spotify_playlist_id'

    # Spotify authentication
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
        client_id=SPOTIFY_CLIENT_ID,
        client_secret=SPOTIFY_CLIENT_SECRET,
        redirect_uri=SPOTIFY_REDIRECT_URI,
        scope='playlist-read-private'
    ))

    # Get Spotify playlist tracks
    print("Retrieving Spotify playlist tracks...")
    tracks = get_spotify_playlist_tracks(sp, SPOTIFY_PLAYLIST_ID)
    print(f"Found {len(tracks)} tracks in the Spotify playlist.")

    # Initialize YouTube Music with authenticated headers
    ytmusic = YTMusic('oauth.json')

    # Create a new YouTube Music playlist
    playlist_name = 'Your Playlist Name'  # Replace with your desired playlist name
    playlist_description = 'Created from Spotify playlist'
    privacy_status = 'PRIVATE'  # Choose 'PRIVATE', 'PUBLIC', or 'UNLISTED'
    print("Creating YouTube Music playlist...")
    ytm_playlist_id = ytmusic.create_playlist(
        playlist_name,
        playlist_description,
        privacy_status=privacy_status
    )
    print(f"YouTube Music playlist '{playlist_name}' created with ID: {ytm_playlist_id}")

    # For each track, search on YouTube Music and add to playlist
    for item in tracks:
        track = item['track']
        artist_names = ', '.join([artist['name'] for artist in track['artists']])
        track_name = track['name']
        query = f"{track_name} {artist_names}"
        print(f"Searching for '{track_name}' by {artist_names} on YouTube Music...")
        search_results = ytmusic.search(query, filter='songs')
        if search_results:
            best_match = search_results[0]
            video_id = best_match['videoId']
            ytmusic.add_playlist_items(ytm_playlist_id, [video_id])
            print(f"Added '{track_name}' by {artist_names} to YouTube Music playlist.")
        else:
            print(f"Could not find '{track_name}' by {artist_names} on YouTube Music.")
        time.sleep(1)  # Sleep to respect rate limits

if __name__ == '__main__':
    main()
