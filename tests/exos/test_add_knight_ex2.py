from exos.exo_02 import add_knight

def test_add_knight_to_empty_kingdom():
    kingdom = []
    knight = "Lancelot"
    kingdom = add_knight(knight, kingdom)
    assert kingdom == ["Lancelot"]

def test_add_knight_to_small_kingdom():
    kingdom = ["Arthur", "Merlin"]
    knight = "Lancelot"
    kingdom = add_knight(knight, kingdom)
    assert kingdom[-1] == "Lancelot"
    assert len(kingdom) == 3

def test_add_knight_new_kingdom():
    knight = "Lancelot"
    kingdom = add_knight(knight)
    assert kingdom == ["Lancelot"]

def test_add_knights_to_new_kingdom():
    knight = "Lancelot"
    other_kniught = "Robin"
    kingdom = add_knight(knight)
    kingdom = add_knight(other_kniught, kingdom)
    assert kingdom == ["Lancelot", "Robin"]

