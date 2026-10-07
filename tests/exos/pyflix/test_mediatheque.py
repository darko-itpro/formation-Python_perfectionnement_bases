import pytest
from pylib.pyflix.mediatheque import TvShow, DuplicateEpisode


def test_name_on_show_creation():
    name = "one piece"
    show = TvShow(name)

    assert show.name == "One Piece"

def test_episodes_on_show_creation():
    name = "one piece"
    show = TvShow(name)
    assert show.episodes == []

@pytest.fixture
def show():
    return TvShow("one piece")

def test_ass_first_episode(show):
    show.add_episode("Grand line", 1, 2)

    assert len(show.episodes) == 1
    assert show.episodes[0].title == "Grand line"

def test_same_episode_must_raise(show):

    show.add_episode("Grand line", 1, 2)

    with pytest.raises(DuplicateEpisode):
        show.add_episode("Grand line", 1, 2)
