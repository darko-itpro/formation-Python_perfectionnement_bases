from exos.exo_02 import add_knight

def test_add_knight_without_kingdom():
    kingdom = add_knight("Arthur")
    assert kingdom == ["Arthur"]

def test_add_knight_to_kingdom():
    camelot = ["Merlin"]
    kingdom = add_knight("Arthur", camelot)
    assert len(kingdom) == 2
    assert "Arthur" in kingdom

def test_add_different_new_kingdoms():
    k1 = add_knight('Conan')
    k2 = add_knight('Gandalf')

    assert k1 == ["Conan"]