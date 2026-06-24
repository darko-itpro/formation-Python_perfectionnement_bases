from pylib.pyflix.mediatheque import TvShow


def test_show_title_case():
    my_show = TvShow("one piece")
    assert my_show.name == "One Piece"
