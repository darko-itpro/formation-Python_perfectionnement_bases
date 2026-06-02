from exos.exo_01 import add_knight

def test_add_knight():
    camelot = []

    assert add_knight(camelot, 'Lancelot') == ["Lanelot"]

def test_add_2_knight():
    camelot = []
    add_knight(camelot, 'Lancelot')

    assert add_knight(camelot, "Robin") == ["Lancelot", "Robin"]
