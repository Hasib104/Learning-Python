
from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import pprint

client_ID = "8c5e5da0ad1140eeb3e8d46544aa2e5b"
spotify_auth = "a5022721b3f9433b81691a4b62b862e7"
my_app_url = "https://developer.spotify.com/dashboard/applications/8c5e5da0ad1140eeb3e8d46544aa2e5b"

time = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
print(time)

response = requests.get(url=f"https://www.billboard.com/charts/hot-100/{time}")
web_response = response.text
#print(web_response)

soup = BeautifulSoup(web_response, "html.parser")

all_songs = soup.find_all(name="span", class_="chart-element__information__song text--truncate color--primary")
#print(all_songs)

all_songs_list = [song.getText() for song in all_songs]
all_songs_list = all_songs_list
print(all_songs_list)

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=client_ID,
        client_secret=spotify_auth,
        show_dialog=True,
        cache_path="token.txt"
    )
)
user_id = sp.current_user()
#print(user_id)
user_id = sp.current_user()["id"]
#print(user_id)

song_uris = []
year = time.split("-")[0]
for song in all_songs_list:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    #print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")
#print(song_uris)
playlist = sp.user_playlist_create(user=user_id, name=f"{time} Billboard 100", public=False)
print(playlist)

sp.user_playlist_add_tracks(user=user_id, playlist_id=playlist["id"], tracks=song_uris)