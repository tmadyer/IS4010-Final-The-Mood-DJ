import pytest
from src import logic
import pandas as pd

def test_analyze_emotion_dev_mode():
    """
    Tests that analyze_emotion returns the mock emotion in dev mode.
    """
    assert logic.analyze_emotion(None, dev_mode=True) == "happy"

def test_get_playlist_for_each_emotion():
    """
    Tests that get_playlist returns a valid playlist for every defined emotion.
    """
    for emotion in logic.PLAYLISTS.keys():
        playlist = logic.get_playlist(emotion)
        assert isinstance(playlist, pd.DataFrame)
        assert not playlist.empty
        assert len(playlist) <= 5
        assert set(playlist.columns) == {"track_name", "artist_name", "album_name"}

def test_get_playlist_unknown_emotion():
    """
    Tests that get_playlist returns the neutral playlist for an unknown emotion.
    """
    playlist = logic.get_playlist("unknown_emotion")
    assert isinstance(playlist, pd.DataFrame)
    assert not playlist.empty
    # It should pull from the neutral playlist
    neutral_track_names = [song['track_name'] for song in logic.PLAYLISTS['neutral']]
    assert playlist.iloc[0]['track_name'] in neutral_track_names

def test_get_playlist_returns_dataframe():
    """
    Tests that get_playlist always returns a pandas DataFrame.
    """
    playlist = logic.get_playlist("happy")
    assert isinstance(playlist, pd.DataFrame)

    playlist = logic.get_playlist("non_existent_emotion")
    assert isinstance(playlist, pd.DataFrame)
