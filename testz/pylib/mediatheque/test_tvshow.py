import pytest
from pylib.pyflix.mediatheque_correction import TvShow

def test_create_show():
    my_show = TvShow("arcane")
    assert my_show.name == "Arcane"
    assert len(my_show.episodes) == 0

@pytest.fixture
def empty_tvshow():
    return TvShow("Arcane")

@pytest.fixture
def tvshow_with_episodes(empty_tvshow):
    empty_tvshow.add_episode("Sisters", 1, 1, )
    empty_tvshow.add_episode("Hexcorp", 2, 1, )
    empty_tvshow.add_episode("Undergrouds", 1, 2, )
    return empty_tvshow

def test_can_add_one_episode(empty_tvshow):
    my_show = empty_tvshow
    my_show.add_episode("Sisters", 1, 1, )

    assert len(my_show.episodes) == 1
    assert my_show.episodes[0].title == "Sisters"

def test_duplicate_must_raise(tvshow_with_episodes):
    my_show = tvshow_with_episodes

    with pytest.raises(ValueError):
        my_show.add_episode("Sisters", 1, 1, )

def test_episodes_should_not_be_altered(tvshow_with_episodes):
    my_show = tvshow_with_episodes
    playlist = my_show.episodes
    playlist.append("toto")

    assert len(my_show.episodes) == 1