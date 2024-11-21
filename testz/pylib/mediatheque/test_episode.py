import pytest
from pylib.pyflix.mediatheque_correction import Episode

def test_episodes_equal_on_number_season_number():
    ep1 = Episode("titre", 1, 1)
    ep2 = Episode("titre autre", 1, 1)

    assert ep1 == ep2