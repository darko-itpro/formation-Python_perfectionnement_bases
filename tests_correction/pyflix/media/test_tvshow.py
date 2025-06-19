import pytest

from pylib.pyflix.mediatheque_correction import TvShow, Episode

def test_name_for_show_creation():
    tvshow = TvShow('for all mankind')
    assert tvshow.name == 'For All Mankind'

def test_episodes_access():
    tvshow = TvShow('for all mankind')
    assert tvshow.episodes == []

def test_add_episode():
    tvshow = TvShow('for all mankind')
    tvshow.add_episode("to the moon", 1, 1)
    assert len(tvshow.episodes) == 1
    assert tvshow.episodes[0].title == 'To The Moon'

def test_duplicate_episode_must_raise():
    tvshow = TvShow('for all mankind')
    tvshow.add_episode("to the moon", 1, 1)
    with pytest.raises(ValueError):
        tvshow.add_episode("to the moon", 1, 1)
