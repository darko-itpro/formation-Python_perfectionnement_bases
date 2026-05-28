import pytest

from pylib.pyflix.mediatheque import TvShow

def test_show_title():
    my_show = TvShow("one piece")
    assert my_show.name == "One Piece"

def test_has_episodes():
    my_show = TvShow("one piece")
    assert my_show.episodes == []

def test_add_one_episode():
    my_show = TvShow("one piece")
    my_show.add_episode("Grand Line", 1, 1)
    assert len(my_show.episodes) == 1
    assert my_show.episodes[0].title == "Grand Line"

def test_add_two_episodes():
    my_show = TvShow("one piece")
    my_show.add_episode("Grand Line", 1, 1)
    my_show.add_episode("Not a Crew", 2, 1)
    assert len(my_show.episodes) == 2
    assert my_show.episodes[0].title == "Grand Line"
    assert my_show.episodes[1].title == "Not a Crew"

def test_add_existing_episode_must_raise():
    my_show = TvShow("one piece")
    my_show.add_episode("Grand Line", 1, 1)
    with pytest.raises(ValueError):
        my_show.add_episode("Grand Line", 1, 1)

def test_episodes_should_not_be_modified():
    my_show = TvShow("one piece")
    my_show.episodes.append('toto')
    assert len(my_show.episodes) == 0
    