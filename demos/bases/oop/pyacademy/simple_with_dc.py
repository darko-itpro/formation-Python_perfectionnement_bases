from dataclasses import dataclass, field

class DuplicateStudentError(ValueError):
    pass


class TrainingFullError(ValueError):
    pass


@dataclass(frozen=True)
class Student:
    name: str
    st_id: str
    title: str
    company: str
    price: float = field(default=None)

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False

        return self.st_id == other.st_id



class Training:
    def __init__(self, subject, description, price, duration, max_seats=12):
        self.subject = subject
        self.description = description
        self.price = price
        self.duration = duration
        self.max_seats = max_seats
        self.students = []

    def add_student(self, student: Student):
        if len(self.students) >= self.max_seats:
            raise TrainingFullError(f"Can't add student, training {self.subject} full")

        if student in self.students:
            raise DuplicateStudentError(f"Student {student.name} already in training")

        self.students.append(student)
