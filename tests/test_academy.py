import pytest
from demos.academy import Training

def test_training_creation():
    training = Training("python perfectionnement", 3)

    assert training.subject == "Python Perfectionnement"
    assert len(training.students) == 0


@pytest.fixture
def empty_training_3_seats():
    return Training("python perfectionnement", 3, seats=3)

@pytest.fixture
def training_3_seats_2_students(empty_training_3_seats):
    training = empty_training_3_seats

    training.add_student("Riri")
    training.add_student("Fifi")

    return training


def test_add_one_student(empty_training_3_seats):
    training = empty_training_3_seats

    training.add_student("John")

    assert len(training.students) == 1


def test_overbooking_must_raise(training_3_seats_2_students):
    training = training_3_seats_2_students

    training.add_student("Loulou")

    with pytest.raises(ValueError, match="Training full"):
        training.add_student("Donald")


def test_has_seats_for_new_training(empty_training_3_seats):
    training = empty_training_3_seats

    assert training.has_seats_left() is True


def test_has_no_seats_after_completing(training_3_seats_2_students):
    training = training_3_seats_2_students

    training.add_student("John")

    assert training.has_seats_left() is False
