import exos.exo_01 as module

def test_add_first_knight():
    module.add_knight("Lancelot")

    assert module.kingdom == ["Lancelot"]
    assert module.count == 1

def test_add_two_knights():
    module.add_knight("Lancelot")
    module.add_knight("Robin")

    assert module.kingdom == ["Lancelot, Robin"]
    assert module.count == 2
