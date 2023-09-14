class DuplicateStudentError(ValueError):
    pass

class Student:
    def __init__(self, name, st_id, title, company, price):
        self.name = name
        self.st_id = st_id
        self.title = title
        self.company = company
        self.price = price

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False

        return (self.name, self.company) == (other.name, other.company)


class Training:
    def __init__(self, subject, description, price, duration, max_seats=12):
        self.subject = subject
        self.description = description
        self.price = price
        self.duration = duration
        self.max_seats = max_seats
        self.students = []

    def add_student(self, student:Student):
        if student in self.students:
            raise DuplicateStudentError(f"Student {student.name} already in training")
        self.students.append(student)
