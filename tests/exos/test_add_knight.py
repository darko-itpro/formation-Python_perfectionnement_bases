from exos import exo_01 as e

def test_add_one_knight():
    e.add_knight("Lancelot")
    assert e.kingdom == ["Lancelot"]
    assert e.count == 1
