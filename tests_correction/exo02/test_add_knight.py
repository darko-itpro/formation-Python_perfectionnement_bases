from exos_correction.exo_02 import add_knight

def test_add_empty_kingdom():
    kingdom = add_knight("Lancelot")
    assert len(kingdom) == 1

def test_add_existing_empty_kingdom():
    aquilonia = []
    assert len(aquilonia) == 0
    kingdom = add_knight("Conan", aquilonia)
    assert len(aquilonia) == 0
    assert len(kingdom) == 1

def test_add_existing_little_kingdom():
    camelot = ["Arthur", "Lancelot"]
    kingdom = add_knight("Robin", camelot)
    assert len(kingdom) == 3

def test_add_empty_kingdom_with_more():
    kingdom = add_knight("Conan")
    assert len(kingdom) == 1
    print(kingdom)
    kingdom = add_knight("Subotai", kingdom)
    assert len(kingdom) == 2


