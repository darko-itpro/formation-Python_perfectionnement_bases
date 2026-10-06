import pytest
from pylib.training import Training

def test_crete_training():
    t = Training("python", 5)
    assert t.subject == "Python"
    assert t.students == []

@pytest.fixture
def training():
    return Training("python", 5)

@pytest.fixture
def add_3_students(training):
    training.add_student("Arthur")
    training.add_student("Merlin")
    training.add_student("Lancelot")


def test_truc(training, add_3_students):
    assert len(training.students) == 3


def test_add_first_student(training):
    training.add_student("Arthur")
    assert training.students == ["Arthur"]

def test_duplicate_students_must_raise(training):
    training.add_student("Arthur")
    with pytest.raises(ValueError, match="^Student Arthur already exists$"):
        training.add_student("Arthur")
