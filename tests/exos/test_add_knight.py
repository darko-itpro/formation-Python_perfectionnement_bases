from exos.exo_01 import add_knight, kingdom

def test_add_knight():
    add_knight("Lancelot")
    assert len(kingdom) == 1

def test_another_add_knight():
    add_knight("Lancelot")
    assert len(kingdom) == 1
