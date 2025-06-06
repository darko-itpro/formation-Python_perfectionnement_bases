import pytest
from exos_correction.pyflix.mediatheque import TvShow, Episode, Playlist

def test_title():
    show = TvShow("for all mankind")
    assert show.name == "For All Mankind"


@pytest.fixture
def empty_show():
    return TvShow("for all mankind")

@pytest.fixture
def playlist():
    return Playlist("Ma playlist")


def test_got_episodes_attr(empty_show):
    assert hasattr(empty_show, "add_episode")
    assert callable(getattr(empty_show, "add_episode"))

    assert len(empty_show.episodes) == 0

def test_can_add_episodes(empty_show):
    empty_show.add_episode("To the moon", 2, 3)
    assert empty_show.episodes[0].title == "To the moon"


def test_duplicate_episode_must_raise(empty_show):
    empty_show.add_episode("To the moon", 2, 3)
    with pytest.raises(ValueError, match="Duplicate episode"):
        empty_show.add_episode("To the moon", 2, 3)

def test_fixture_playlist(playlist):
    assert len(playlist.episodes) == 0

class TestPlus:
    @pytest.fixture(autouse=True)
    def add_one_episode_to_playlist(self, playlist, one_episode):
        playlist.add_episode(one_episode)

    def test_fixture_playlist(self, playlist):
        assert len(playlist.episodes) == 1

