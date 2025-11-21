from datetime import datetime, timedelta
from dataclasses import dataclass, field

class StudentNotFoundError(ValueError):
    pass


class DuplicateStudentError(ValueError):
    pass


class UnconsistentDateError(ValueError):
    pass


class TrainingFullError(ValueError):
    pass


@dataclass(frozen=True)
class Training:
    subject: str
    description: str
    price: float
    duration: int
    max_seats: int = field(default=12)

from collections import namedtuple
Training = namedtuple("Training", ('subject', 'description', 'price', 'duration', 'max_seats'),
                      defaults=[12])


class StudentsIterator:
    def __init__(self, students):
        self.students = students.copy()

    def __iter__(self):
        return self

    def __next__(self):
        try:
            student = self.students.pop(0)
            return student

        except IndexError:
            raise StopIteration("End of collection")


class TrainingSession:
    def __init__(self, training: Training, start_date: datetime, duration: int):
        self._training = training
        self.start_date = start_date
        self.duration = duration
        self._coach = None
        self._students = []

    def __len__(self):
        return len(self._students)

    def __contains__(self, item):
        return item in self._students

# Accéder à un stagiaire par un indice ou un identifiant ne fait pas vraiment sens dans ce modèle,
# cette méthode ne sera donc pas implantée.
    # def __getitem__(self, item):
    #     print(type(item))
    #     print(item)

    def __iter__(self):
        return StudentsIterator(self._students.copy())

    @property
    def subject(self):
        return self._training.subject

    @property
    def coach(self):
        return self._coach

    @property
    def description(self):
        return self._training.description

    @property
    def available_seats(self):
        available_seats = self._training.max_seats - len(self._students)
        return available_seats if available_seats >= 0 else 0

    @property
    def students(self):
        return self._students.copy()

    @property
    def start_date(self):
        return self._start_date

    @property
    def end_date(self):
        return self._start_date + timedelta(days=self.duration)

    @start_date.setter
    def start_date(self, new_date:datetime):
        if new_date.weekday() + self.duration > 4:
            raise UnconsistentDateError(f"Start date {new_date} not compatible with training duration")

        self._start_date = new_date

    @start_date.deleter
    def start_date(self):
        self._start_date = None

    def add_or_update_coach(self, coach):
        self._coach = coach

    def add_student(self, student):
        if len(self.students) >= self.max_seats:
            raise TrainingFullError(f"Can't add student, training {self.subject} full")

        if student in self.students:
            raise DuplicateStudentError(f"Student {student.name} already in training")

        self._students.append(student)

    def remove_student(self, first_name: str, last_name: str):
        for index, student in self.students:
            if (first_name, last_name) == (student.first_name, student.last_name):
                return self.students.pop(index)

        raise StudentNotFoundError(f"Student {first_name} {last_name} not found in training")
