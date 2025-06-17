from exos_correction.exo_01 import add_knight, kingdom

def test_add_first_knight():
    add_knight("Lancelot") # Act

    assert len(kingdom) == 1 # Assert
