
from exos_correction.exo_01 import add_knight, kingdom

def test_element_to_existing_kingdom():
    assert len(kingdom) == 0
    add_knight("lancelot")
    assert len(kingdom) == 1

