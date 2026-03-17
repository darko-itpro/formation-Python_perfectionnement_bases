import pytest
from exos import exo_01 as e

def test_add_one_knight():
    new_kingdom = e.add_knight("Lancelot", e.camelot)
    assert e.camelot == []
    assert new_kingdom == ["Lancelot"]
    assert e.count == 1


@pytest.mark.skip(reason="Test foireux pour démo")
def test_add_two_knight():
    e.add_knight("Lancelot", e.camelot)
    e.add_knight("Robin", e.camelot)
    assert e.camelot == ["Lancelot", "Robin"]
    assert e.count == 2

