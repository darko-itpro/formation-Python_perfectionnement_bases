import pytest
from pylib.pyflix.mediatheque import TvShow, DuplicateEpisode

# Test init
def test_show_title_case():
    my_show = TvShow("one piece")
    assert my_show.name == "One Piece"

# Test add_episode

@pytest.fixture
def my_show():
    return TvShow("one piece")

@pytest.fixture
def with_3_episodes(my_show):
    my_show.add_episode("Grand Line", 2, 1)
    my_show.add_episode("The One Piece", 2, 4)
    my_show.add_episode("The Clown", 1, 1)

def test_episodes_it_attribute(my_show):
    assert my_show.episodes == []

def test_add_one_episode(my_show):
    my_show.add_episode("Grand Line", 2, 1)
    assert len(my_show.episodes) == 1
    assert my_show.episodes[0].title == "Grand Line"

def test_add_episode_to_show_with_episodes(my_show, with_3_episodes):
    my_show.add_episode("The Climb", 2, 2)
    assert len(my_show.episodes) == 4

def test_duplicate_episode_must_raise(my_show):
    my_show.add_episode("Grand Line", 2, 1)

    with pytest.raises(DuplicateEpisode):
        my_show.add_episode("Grand Line", 2, 1)