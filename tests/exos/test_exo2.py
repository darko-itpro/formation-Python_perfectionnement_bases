from exos.exo_02 import add_knight

def test_add_knight_to_kingdom():
    camelot = ["Arthur"]
    camelot = add_knight("Lancelot", camelot)
    assert len(camelot) == 2

def test_add_knight_to_new_kingdom():
    camelot = add_knight("Lancelot")
    assert len(camelot) == 1

def test_add_knight_to_new_kingdom_again():
    camelot = add_knight("Lancelot")
    assert len(camelot) == 1
