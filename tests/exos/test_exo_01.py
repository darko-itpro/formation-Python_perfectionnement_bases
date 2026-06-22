from exos import exo_01 as e1

def test_add_one_knight():
    e1.add_knight("Lancelot")
    assert e1.kingdom == ["Lancelot"]


def test_add_two_knights():
    e1.kingdom = []
    e1.add_knight("Lancelot")
    e1.add_knight("Robin")
    assert e1.kingdom == ["Lancelot", "Robin"]
