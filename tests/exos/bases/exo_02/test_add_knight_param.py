import pytest

from exos.exo_02 import add_knight

def test_add_knight_no_kingdom():
    kingdom = add_knight("Lancelot")
    assert kingdom == ["Lancelot"]

def test_add_knight_new_kingdom_again():
    coruscant = add_knight("Luke")
    assert coruscant == ["Luke"]

test_data_kingdom = [ # knight, kingdom, size, first_element
    ("Lancelot", [], 1, "Lancelot"),
    ("Lancelot", ["Arthur"], 2, "Arthur"),
    ("Lancelot", ["Arthur", "Merlin"], 3, "Arthur"),
]

@pytest.mark.parametrize(["knight", "kingdom", "size", "first_element"], test_data_kingdom)
def test_add_knight_existing_kingdom(knight, kingdom, size, first_element):
    kingdom = add_knight(knight, kingdom)
    assert len(kingdom) == size
    assert kingdom[-1] == knight
    assert kingdom[0] == first_element
