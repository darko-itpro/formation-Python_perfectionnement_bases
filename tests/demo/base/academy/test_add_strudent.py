import pytest
from demos.bases.academy import Training

@pytest.fixture
def training():
    return Training("python, bases", 5, 5)

@pytest.fixture
def fill_training_to_full(training):
    training.add_student("John Doe")
    training.add_student("Jeanette Doe")
    training.add_student("Jane Doe")
    training.add_student("John Paul")
    training.add_student("John Paulette")

def test_training_full_must_raise(training, fill_training_to_full):
    with pytest.raises(ValueError):
        training.add_student("John D.")


def test_add_first_student(training):
    training.add_student("John Doe")

    assert training.students == ["John Doe"]

def test_add_several_students(training):
    training.add_student("John Doe")
    training.add_student("Jane Doe")

    assert training.students == ["John Doe", "Jane Doe"]
