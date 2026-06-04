import pytest
from pylib.pyflix.mediatheque import TvShow

def test_title_is_titlized():
    show = TvShow("lucky luke")
    assert show.name == "Lucky Luke"

def test_episodes_is_attr():
    show = TvShow("lucky luke")

    assert len(show.episodes) == 0

    # Pour le test, ligne précédente ou suivantes

    assert hasattr(show, "episodes")
    assert not callable(show.episodes)

def test_add_episode():
    show = TvShow("lucky luke")

    show.add_episode("Daisy Town", 1, 1)

    assert len(show.episodes) == 1
    assert show.episodes[0].title == "Daisy Town"

def test_add_duplicate_must_raise():
    show = TvShow("lucky luke")
    show.add_episode("Daisy Town", 1, 1)

    with pytest.raises(ValueError):
        show.add_episode("Daisy Town", 1, 1)
