import pytest
from pylib.pyflix.mediatheque import TvShow, DuplicateEpisode


def test_create_show():
    my_show = TvShow("My show")

    assert my_show.name == "My Show"
    assert len(my_show.episodes) == 0


@pytest.fixture
def my_show():
    return TvShow("My show")

@pytest.fixture
def add_1_episode_to_show(my_show):
    my_show.add_episode("first", 1, 1)


def test_add_first_episode(my_show):
    my_show.add_episode("title", 1, 1)
    assert len(my_show.episodes) == 1

def test_add_two_episode(my_show):
    my_show.add_episode("title 1", 1, 1)
    my_show.add_episode("title 2", 1, 2)
    assert len(my_show.episodes) == 2
    assert my_show.episodes[0].title == "title 1"
    assert my_show.episodes[1].title == "title 2"

def test_duplicate_episode_must_raise(my_show):
    my_show.add_episode("title 1", 1, 1)
    with pytest.raises(DuplicateEpisode):
        my_show.add_episode("title 1", 1, 1)
