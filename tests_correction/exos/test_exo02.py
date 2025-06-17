from exos_correction.exo_02 import add_knight

def test_add_first_knight_empty_kingdom():
    kingdom = []
    kingdom = add_knight("Lancelot", kingdom)
    assert len(kingdom) == 1
    assert kingdom[0] == "Lancelot"

def test_add_knight_without_kingdom():
    kingdom = add_knight("Lancelot")
    assert len(kingdom) == 1
    assert kingdom[0] == "Lancelot"

# Pour paramètre optionnel
def test_add_knight_without_kingdom_again():
    kingdom = add_knight("Lancelot")
    assert len(kingdom) == 1
    assert kingdom[0] == "Lancelot"
