test_data = [({"title": "The Conjugal Configuration", "duration": 20, "viewed": True}, True),
             ({"title": "The Conjugal Configuration", "duration": 20, "viewed": 3}, True),
             ({"title": "The Conjugal Configuration", "duration": 20, "viewed": 3, "year": 2019},
              True),
             ({"title": "The Conjugal Configuration", "duration": 20, "viewed": False}, False),
             ({"title": "The Conjugal Configuration", "duration": 20, "viewed": 0}, False),
             ({"title": "The Conjugal Configuration", "duration": 20}, False),
             ({"title": "The Conjugal Configuration", "duration": 20, "year": 2018}, False),
             ]

import pytest
from demos.bases.episode_helper import is_viewed

@pytest.mark.parametrize("episode, expected", test_data)
def test_is_viewed(episode, expected):
    assert is_viewed(episode) is expected


