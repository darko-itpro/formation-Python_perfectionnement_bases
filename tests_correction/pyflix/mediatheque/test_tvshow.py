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

def test_can_add_episode():
    show = TvShow('for all mankind')
    show.add_episode('To the moon', 1, 1)
    assert len(show.episodes) == 1
    assert show.episodes[0].title == 'To the moon'


def test_duplicate_must_raise():
    show = TvShow('for all mankind')
    show.add_episode('To the moon', 1, 1)
    with pytest.raises(ValueError):
        show.add_episode('To the moon', 1, 1)