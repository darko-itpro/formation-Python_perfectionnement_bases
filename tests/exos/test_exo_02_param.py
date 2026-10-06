import pytest
from exos.exo_02 import add_knight

test_data = [ # (knight, kingdom, result)
    ("Arthur", [], 1),
    ("Arthur", ["Merlin"], 2),
    ("Lancelot", ["Arthur", "Merlin"], 3),
]

@pytest.mark.parametrize(("knight", "kingdom", "size"), test_data)
def test_add_knight_to_kingdom(knight, kingdom, size):
    kingdom = add_knight(knight, kingdom)
    assert len(kingdom) == size

