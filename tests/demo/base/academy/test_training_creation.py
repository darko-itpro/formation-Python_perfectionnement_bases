import pytest
from demos.bases.academy import Training

def test_low_duration_must_raise():
    with pytest.raises(ValueError, match="Duration must"):
        Training("python, bases", 0, 10)

def test_create_simple_training():
    training = Training("python, bases", 5, 10)
    assert training.subject == 'Python, Bases'
    assert training.duration == 5
    assert training.max_seats == 10
    assert training.students == []

def test_create_training_without_seats():
    training = Training("python, bases", 5)
    assert training.subject == 'Python, Bases'
    assert training.duration == 5
    assert training.max_seats == 12
    assert training.students == []