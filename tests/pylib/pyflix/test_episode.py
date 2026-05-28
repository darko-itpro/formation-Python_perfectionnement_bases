from pylib.pyflix.mediatheque import Episode

def test_episodes_are_equal():
    ep1 = Episode("Grand Line", 1, 1)
    ep2 = Episode("Grand Line", 1, 1)
    assert ep1 == ep2
