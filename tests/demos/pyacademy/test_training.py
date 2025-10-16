import pytest
from demos.pyacademy.training import Training, Student, DuplicateStudentError

def test_training_creation():
    training = Training("Python experts", "", 3000, 4, 12)

    assert len(training.students) == 0
    assert training.subject == "Python Experts"

@pytest.fixture
def training():
    return Training("Python experts", "", 3000, 4, 12)

@pytest.fixture
def student():
    return Student('John Doe', "jd234", "Dr.", "", None)

@pytest.fixture
def add_one_training_to_student(training, student):
    training.add_student(student)

def test_first_student(training, student):
    training.add_student(student)

    assert len(training.students) == 1
    assert training.students[0].name == "John Doe"

@pytest.mark.skip(reason="not implemented")
@pytest.mark.usefixtures("add_one_training_to_student")
def test_add_student_to_non_empty_training(training):
    assert len(training.students) == 0

@pytest.mark.usefixtures("add_one_training_to_student")
def test_duplicate_student_must_raise(training, student):
    with pytest.raises(DuplicateStudentError, match="Student J... Doe"):
        training.add_student(student)

