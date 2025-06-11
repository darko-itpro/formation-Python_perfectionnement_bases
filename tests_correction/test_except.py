import pytest

def test_is_raised():
    with pytest.raises(ValueError):
        raise ValueError("test")
