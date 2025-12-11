import pytest
from pylib.pyflix.mediatheque import TvShow

def test_show_creation():
    show = TvShow("stranger code")
    assert show.name == "Stranger Code"
    assert show.episodes == []

@pytest.fixture
def show():
    return TvShow("stranger code")

@pytest.fixture
def add_2_episodes_to_show(show):
    show.add_episode("Creating the project", 1, 1)
    show.add_episode("First meeting", 2, 1)

def test_add_first_epiosde(show):
    show.add_episode("Creating the project", 1, 1)

    assert len(show.episodes) == 1
    assert show.episodes[0].title == "Creating the project"

def test_add_duplicate_episode_must_raise(show):
    show.add_episode("Creating the project", 1, 1)

    with pytest.raises(ValueError):
        show.add_episode("Creating the project", 1, 1)
