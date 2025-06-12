import pytest
from exos_correction.pylib.mediatheque import TvShow

title_values = [
    ('for all mankind', "For All Mankind"),
    ('FOR ALL MANKIND', "For All Mankind"),
]


@pytest.mark.parametrize('title, expected', title_values)
def test_title_case(title, expected):
    show = TvShow(title)
    assert show.name == expected


def test_has_empty_attribute_episodes():
    show = TvShow('for all mankind')
    assert hasattr(show, 'episodes')
    assert len(show.episodes) == 0


@pytest.fixture
def show():
    return TvShow('for all mankind')


@pytest.fixture
def show_with_one_episode(show):
    show.add_episode('To the moon', 1, 1)
    return show

def test_can_add_episode(show_with_one_episode):
    assert len(show_with_one_episode.episodes) == 1
    assert show_with_one_episode.episodes[0].title == 'To the moon'


def test_duplicate_must_raise(show):
    show.add_episode('To the moon', 1, 1)
    with pytest.raises(ValueError):
        show.add_episode('To the moon', 1, 1)

def test_assign_eppisodes_must_raise(show):
    with pytest.raises(AttributeError):
        show.episodes = []

def test_episodes_should_not_be_added(show):
    show.add_episode('To the moon', 1, 1)
    show.episodes.append("toto")
    assert len(show.episodes) == 1

def test_update_title_must_match_case(show):
    show.name = "for all manKinD"
    assert show.name == "For All Mankind"







