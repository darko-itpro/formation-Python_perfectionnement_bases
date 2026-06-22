from exos.exo_02 import add_knight

def test_add_knight_without_kingdom():
    kingdom = add_knight("Lancelot")
    assert kingdom == ["Lancelot"]
    assert len(kingdom) == 1
    assert kingdom[0] == "Lancelot"

def test_add_one_knight_to_existing_kingdom():
    kingdom = ["Lancelot", "Robin"]
    kingdom = add_knight("Bohort", kingdom)
    assert len(kingdom) == 3
    assert kingdom[-1] == "Bohort"

def test_add_two_new_kingdom():
    kingdom = add_knight("LAncelot")
    assert kingdom == ["LAncelot"]

    kingdom = add_knight("Conan")
    assert kingdom == ["Conan"]