import spotipy
from spotipy.oauth2 import SpotifyOAuth
from bs4 import BeautifulSoup
import requests

client_id = "e574cd04ec284833a26a3183dd93b940"
client_secret = "3561a9bd041f485fb868e8797372448e"
redirect_uri = "https://blessingchuks.tech/"
scope = "playlist-modify-public"


sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri, scope=scope))

# sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri, scope=scope))

def search_track(track_name):
    # search for track by title
    results = sp.search(q=track_name, type="track", limit=1)

    # add track to list
    if len(results["tracks"]["items"]) > 0:
        track_uri = results["tracks"]["items"][0]["uri"]
        # print(f"Found {track_name} on Spotify! Track URI: {track_uri}")
        return track_uri
    else:
        # print(f"No tracks found with the title {track_name}.")
        return None

date = input("which year do you want to travel to? type the date in this format YYYY-MM-DD: ")


response = requests.get("https://www.billboard.com/charts/hot-100/" + date + "/")
# response = requests.get("https://www.billboard.com/charts/hot-100/2017-01-01/")
music = response.text
soup = BeautifulSoup(music, "html.parser")
musics = soup.find_all(name="h3", class_="a-no-trucate")
all_musics = []

for song in musics:
    a = song.getText().replace('\n', '').replace('\t', '')
    all_musics.append(a)



track_uris = []
for music in all_musics:
    track_uri = search_track(music)
    if track_uri is not None:
        track_uris.append(track_uri)
# print(track_uris)

# create new playlist
user_id = sp.me()["id"]   # get user ID
playlist_name = "My New Playlist"
playlist_desc = "A new playlist created with Spotipy!"

playlist = sp.user_playlist_create(user=user_id, name=playlist_name, public=True, description=playlist_desc)

sp.playlist_add_items(playlist["id"], track_uris)
print("Playlist created:", playlist["external_urls"]["spotify"])