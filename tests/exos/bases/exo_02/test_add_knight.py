import pytest
from exos.exo_02 import add_knight

def test_add_knight_without_kingdom():
    kingdom = add_knight("Lancelot")
    assert len(kingdom) == 1
    assert kingdom == ["Lancelot"]

def test_add_several_new_kingdoms():
    camelot = add_knight("Lancelot")
    aquilonia = add_knight("Conan")
    assert camelot == ["Lancelot"]
    assert aquilonia == ["Conan"]

def test_add_knight_with_empty_kingdom():
    kingdom = []
    k = add_knight("Lancelot", kingdom)
    assert k == ["Lancelot"]
