import pytest
from exos_correction.pyflix.demo_media import is_viewed

test_data = [
    ({'title': 'Star Wars',
      'duration': 121,
      'viewed': 16}, True),
    ({'title': 'Star Wars: Episode I - The Phantom Menace',
      'duration': 136, }, False),
    ({'title': 'Star Wars: Episode I - The Phantom Menace',
      'duration': 136,
      'viewed': 0}, False),
]

@pytest.mark.parametrize('episode, expected', test_data)
def test_viewed(episode, expected):
    assert is_viewed(episode) == expected