from exos.exo_01 import add_knight_right_way

def test_add_knight_empty_kingdom():
    kingdom = []
    count = 0

    assert add_knight_right_way("Robin", kingdom, count) == 1
    assert kingdom == ["Robin"]
    assert count == 0

def test_add_knight_kingdom_with_two():
    kingdom = ["Arthur", "Lancelot"]
    count = 0

    assert add_knight_right_way("Robin", kingdom, count) == 1
    assert kingdom == ["Arthur", "Lancelot", "Robin"]
    assert count == 0
