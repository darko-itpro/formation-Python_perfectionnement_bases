import pytest
from pylib.pyflix.mediatheque import TvShow

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


def test_fixtures(my_show, add_1_episode_to_show):
    assert len(my_show.episodes) == 1


def test_exception_is_raised():
    with pytest.raises(ValueError):
        int("toto")


def test_add_first_episode(my_show):
    my_show.add_episode("title", 1, 1)
    assert len(my_show.episodes) == 1

def test_once_more_add_first_episode(my_show):
    my_show.add_episode("title", 1, 1)
    assert len(my_show.episodes) == 1

