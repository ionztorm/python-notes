"""Spotify playlist generator."""

import datetime

from billboard import get_tracks
from dotenv import load_dotenv
from spotipy import Spotify
from spotipy.oauth2 import SpotifyOAuth

load_dotenv()
parser = "html.parser"


def main() -> None:
    """Get top 100 song titles from a given date and create a spotify playlist."""
    results = get_tracks()
    tracks = results[0]
    week_unformatted = results[1]
    year = week_unformatted.split("-")[0]
    week = datetime.datetime.strptime(week_unformatted, "%Y-%m-%d").strftime("%d %b %Y")
    playlist_name = f"Top 100 chart as on {week}"

    scope = "playlist-modify-public"
    sp = Spotify(auth_manager=SpotifyOAuth(scope=scope))

    user = sp.current_user()
    assert user is not None, "Expected sp.current_user() to return a dictionary"  # noqa: S101
    user_id = user["id"]

    track_uris = []
    for track in tracks:
        query = f"track:{track} year:{year}"
        search_result = sp.search(q=query, type="track", limit=1)
        assert search_result is not None, "Expect sp.search() to return a dictionary"  # noqa: S101
        if not search_result["tracks"]["items"]:
            print(f"Track: {track} not found, skipping..")
            continue
        track_uris.append(search_result["tracks"]["items"][0]["uri"])

    playlist_id = None

    user_playlists = sp.current_user_playlists(limit=50)
    assert user_playlists is not None, "Expect sp.current_user_playlists() to return a dictionary"  # noqa: S101

    for playlist in user_playlists["items"]:
        if playlist["name"].lower() == playlist_name.lower():
            playlist_id = playlist["id"]
        else:
            playlist_data = sp.user_playlist_create(
                user_id,
                public=True,
                collaborative=False,
                name=playlist_name,
                description=playlist_name,
            )
            assert playlist_data is not None, (  # noqa: S101
                "Expected sp.user_playlist_create() to return a dictionary"
            )
            playlist_id = playlist_data["id"]

    sp.playlist_add_items(playlist_id=playlist_id, items=track_uris)


main()
