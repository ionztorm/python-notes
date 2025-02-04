"""Spotipy funcs."""

from dotenv import load_dotenv
from spotipy import Spotify
from spotipy.oauth2 import SpotifyOAuth

load_dotenv()

scope = "playlist-modify-public"
sp = Spotify(auth_manager=SpotifyOAuth(scope=scope))

user = sp.current_user()
assert user is not None, "Expected sp.current_user() to return a dictionary"  # noqa: S101

user_id = user["id"]

print(user_id)
