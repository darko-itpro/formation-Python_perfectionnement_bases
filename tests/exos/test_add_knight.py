import pytest
from exos.exo_02 import add_knight

def test_add_knight_to_empty_kingdom():
    camelot = []
    knight = "Lancelot"

    camelot = add_knight(knight, camelot)

    assert camelot == ["Lancelot"]

def test_add_knight_to_new_kingdom():
    knight = "Lancelot"

    camelot = add_knight(knight)

    assert camelot == ["Lancelot"]

def test_add_knight_to_kingdom_with_king():
    camelot = ["Arthur"]
    knight = "Lancelot"

    camelot = add_knight(knight, camelot)

    assert camelot == ["Arthur", "Lancelot"]

def test_add_knight_to_new_kingdoms():
    knight = "Lancelot"
    warrior = "Conan"

    camelot = add_knight(knight)
    aquilonia = add_knight(warrior)

    assert camelot == ["Lancelot"]
    assert aquilonia == ["Conan"]

def test_exception_raised():
    with pytest.raises(ZeroDivisionError):
        5 / 0