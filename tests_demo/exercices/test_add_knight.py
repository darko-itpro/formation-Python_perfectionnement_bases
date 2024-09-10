from exercices.exo_02 import add_knight

def test_add_knight_without_kingdom():
    kingdom = add_knight('BatMan')
    assert len(kingdom) == 1

def test_add_knight_to_empty_kingdom():
    kingdom = []
    new_kingdom = add_knight('BatMan', kingdom)
    assert len(new_kingdom) == 1

def test_add_knight_to_kingdom_with_knights():
    kingdom = ["Arthur", "Lancelot"]
    new_kingdom = add_knight('BatMan', kingdom)
    assert len(new_kingdom) == 3

def test_something():
    aquilonia = add_knight("Conan")
    gotham = add_knight("BatMan")

    assert len(aquilonia) == 1
    assert len(gotham) == 1