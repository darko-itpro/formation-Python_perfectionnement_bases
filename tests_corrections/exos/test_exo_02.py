from exos_correction.exo_02 import add_knight

def test_add_knight_new_kingdom():
    aquilonia = add_knight("Conan")

    assert len(aquilonia) == 1
    assert aquilonia[0] == "Conan"

def test_add_knight_existing_kingdom():
    camelot = ["Arthur"]
    camelot = add_knight("Merlin", camelot)
    assert len(camelot) == 2

def test_add_again_knight_new_kingdom():
    aquilonia = add_knight("Conan")

    assert len(aquilonia) == 1
    assert aquilonia[0] == "Conan"

