import pytest
from pylib.pyflix.mediatheque import TvShow

def test_show_init():
    myshow = TvShow('dr. who')

    assert myshow.name == "Dr. Who"
    assert len(myshow.episodes) == 0

@pytest.fixture
def empty_show():
    return TvShow('Dr. Who')

def test_add_first_episode(empty_show):
    show = empty_show
    show.add_episode("title", 1, 1)

    assert len(show.episodes) == 1

def test_duplicate_must_raise(empty_show):
    show = empty_show
    show.add_episode("title", 1, 1)

    with pytest.raises(ValueError):
        show.add_episode("title", 1, 1)
