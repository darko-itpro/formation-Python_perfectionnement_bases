import pytest
from exos_correction.pyflix.mediatheque import Episode

@pytest.fixture
def one_episode():
    return Episode("To the moon", 1, 1)

