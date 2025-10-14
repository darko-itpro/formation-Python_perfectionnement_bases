from exos.exo_02 import add_knight

def test_add_knight_with_kingdom():
    camelot = []
    kingdom = add_knight("Lancelot", camelot)
    assert kingdom == ["Lancelot"]

def test_add_knight_with_kingdom_with_knights():
    camelot = ['Perceval', 'Karadoc']
    kingdom = add_knight("Lancelot", camelot)
    assert kingdom == ['Perceval', 'Karadoc', "Lancelot"]


def test_add_knight_without_kingdom():
    kingdom = add_knight("Conan")
    assert kingdom == ["Conan"]

def test_add_more_knight_without_kingdom():
    kingdom1 = add_knight("Conan")
    kingdom2 = add_knight("Subotai")
    assert kingdom2 == ["Subotai"]
