import pytest
from pylib.pyflix.mediatheque import TvShow

@pytest.fixture
def empty_show():
    return TvShow('Dr. Who')

@pytest.fixture
def show_with_episodes(empty_show):
    empty_show.add_episode("Rose", 1, 1)
    empty_show.add_episode("Daleks", 2, 1)
    empty_show.add_episode("Gallyfrey", 1, 2)

    return empty_show


def test_create_show():
    show = TvShow('Dr. who')
    assert show.name == "Dr. Who"

def test_add_first_episode(empty_show):
    empty_show.add_episode("Rose", 1, 1)
    assert len(empty_show.episodes) == 1

def test_add_several_episodes(empty_show):
    empty_show.add_episode("Rose", 1, 1)
    empty_show.add_episode("Daleks", 2, 1)
    empty_show.add_episode("Gallyfrey", 1, 2)
    assert len(empty_show.episodes) == 3

def test_duplicate_episode_must_raise(show_with_episodes):
    with pytest.raises(ValueError):
        show_with_episodes.add_episode("Daleks", 2, 1)
