from exos import exo_01

def test_add_one_knight():
    exo_01.add_knight("Arthur")
    assert exo_01.kingdom == ['Arthur']
    assert exo_01.count == 1

def test_add_one_other_knight():
    exo_01.add_knight("Lancelot")
    assert exo_01.kingdom == ['Lancelot']
    assert exo_01.count == 1
