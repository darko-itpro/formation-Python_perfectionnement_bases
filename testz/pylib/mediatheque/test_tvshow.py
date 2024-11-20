import pytest
from pylib.pyflix.mediatheque_correction import TvShow

def test_create_show():
    my_show = TvShow("arcane")
    assert my_show.name == "Arcane"
    assert len(my_show.episodes) == 0

def test_can_add_one_episode():
    my_show = TvShow("Arcane")
    my_show.add_episode("Sisters", 1, 1, )

    assert len(my_show.episodes) == 1
    assert my_show.episodes[0].title == "Sisters"

def test_duplicate_must_raise():
    my_show = TvShow("Arcane")
    my_show.add_episode("Sisters", 1, 1, )

    with pytest.raises(ValueError):
        my_show.add_episode("Sisters", 1, 1, )

def test_episodes_should_not_be_altered():
    my_show = TvShow("Arcane")
    my_show.add_episode("Sisters", 1, 1, )
    playlist = my_show.episodes
    playlist.append("toto")

    assert len(my_show.episodes) == 1