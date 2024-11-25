from exos_correction.exo_02 import add_knight

def test_add_knight_to_existing_kingdom():
    camelot = []
    camelot = add_knight("Lancelot", camelot)

    assert len(camelot) == 1
    assert camelot[0] == "Lancelot"


def test_add_knight_to_existing_populated_kingdom():
    camelot = ["Arthur", "Merlin"]
    camelot = add_knight("Lancelot", camelot)

    assert len(camelot) == 3
    assert camelot[-1] == "Lancelot"


def test_add_new_kigdom():
    camelot = add_knight("Lancelot")
    assert len(camelot) == 1

def test_add_two_knights_to_new_kingdom():
    camelot = add_knight("Lancelot")
    camelot = add_knight("Robin", camelot)
    assert len(camelot) == 2

