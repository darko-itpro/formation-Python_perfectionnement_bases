from exos.exo_02 import add_knight

def test_add_knight_no_kingdom():
    kingdom = add_knight("Lancelot")
    assert kingdom == ["Lancelot"]

def test_add_knight_existing_kingdom():
    camelot = ["Arthur", "Merlin"]
    camelot = add_knight("Lancelot", camelot)
    assert len(camelot) == 3
    assert camelot[-1] == "Lancelot"

def test_add_knight_new_kingdom_again():
    coruscant = add_knight("Luke")
    assert coruscant == ["Luke"]
