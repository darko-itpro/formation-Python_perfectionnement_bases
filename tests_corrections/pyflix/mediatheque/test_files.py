from pathlib import Path
import pytest

pytestmark = pytest.mark.slow

@pytest.mark.skip(reason="useless without assertion")
def test_about_file(tmp_path):
    d = tmp_path / 'demo'
    d.mkdir()

@pytest.mark.xfail(reason="must fail")
def test_must_fail():
    assert False is True
