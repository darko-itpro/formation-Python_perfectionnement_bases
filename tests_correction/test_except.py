import pytest

def test_is_raised():
    with pytest.raises(ValueError, match="Mon message attendu"):
        raise ValueError("test")
