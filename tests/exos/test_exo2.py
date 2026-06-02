from exos.exo_02 import add_knight

def test_add_knight_to_existing_kingdom():
    camelot = []
    knight = "Lancelot"

    assert add_knight(knight, camelot) == ["Lancelot"]

def test_add_knight_to_new_kingdom():
    knight = "Lancelot"

    assert add_knight(knight) == ["Lancelot"]

def test_add_knights_to_new_kingdoms():
    knight1 = "Lancelot"
    knight2 = "Conan"

    assert add_knight(knight1) == ["Lancelot"]