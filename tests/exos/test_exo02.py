from exos.exo_02 import add_knight

def test_add_knight_without_kingdom():
    kingdom = add_knight("Conan")
    
    assert kingdom == ["Conan"]

def test_add_knight_to_kingdom():
    kingdom = add_knight("Conan", [])
    
    assert kingdom == ["Conan"]

def test_add_knight_to_kingdom_with_people():
    camelot = ["Arthur", "Merlin"]
    kingdom = add_knight("Lancelot", camelot)
    
    assert len(kingdom) == 3
    assert kingdom[-1] == "Lancelot"

def test_once_more():
    camelot = add_knight("Arthur")
    camelot = add_knight("Merlin", camelot)
    assert len(camelot) == 2