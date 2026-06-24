import pytest
from pylib.pyflix.mediatheque import TvShow, DuplicateEpisode


def test_show_title_case():
    my_show = TvShow("one piece")
    assert my_show.name == "One Piece"

def test_episodes_it_attribute():
    my_show = TvShow("one piece")
    assert my_show.episodes == []

def test_add_one_episode():
    my_show = TvShow("one piece")
    my_show.add_episode("Grand Line", 2, 1)
    assert len(my_show.episodes) == 1
    assert my_show.episodes[0].title == "Grand Line"

def test_duplicate_episode_must_raise():
    my_show = TvShow("one piece")
    my_show.add_episode("Grand Line", 2, 1)

    with pytest.raises(DuplicateEpisode):
        my_show.add_episode("Grand Line", 2, 1)