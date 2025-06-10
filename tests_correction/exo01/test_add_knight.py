from exos_correction import exo01

def test_add_one_knight_empty_kingdom():
    exo01.add_knight("lancelot")
    assert len(exo01.kingdom) == 1
    assert exo01.count == 1

