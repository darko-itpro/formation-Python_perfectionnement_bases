import pytest
from pylib.pyflix.mediatheque import TvShow

def test_create_tvshow():
    myshow = TvShow("one piece")
    assert myshow.name == "One Piece"
    assert myshow.episodes == []

@pytest.fixture
def myshow():
    return TvShow("one piece")

def test_one_episode(myshow):
    myshow.add_episode("Grand line", 2, 1)
    assert len(myshow.episodes) == 1
    assert myshow.episodes[0].title == "Grand line"

def test_duplicate_episode_must_raise(myshow):
    myshow.add_episode("Grand line", 2, 1)
    with pytest.raises(ValueError):
        myshow.add_episode("Grand line", 2, 1)
