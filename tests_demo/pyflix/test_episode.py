from pylib.pyflix.mediatheque import Episode

def test_episodes_are_equal_on():
    ep1 = Episode('Rose', 1, 1)
    ep2 = Episode('Rose', 1, 1)

    assert ep1 == ep2