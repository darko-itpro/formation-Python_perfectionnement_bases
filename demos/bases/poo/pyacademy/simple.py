class DuplicateStudentError(ValueError):
    pass


class TrainingFullError(ValueError):
    pass


class Student:
    def __init__(self, name, st_id, title, company, price: None):
        self.name:str = name
        self.st_id:str = st_id
        self.title:str = title
        self.company:str = company
        self.price:float|None = price

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

    def add_student(self, student:Student):
        if len(self.students) >= self.max_seats:
            raise TrainingFullError(f"Can't add student, training {self.subject} full")

        if student in self.students:
            raise DuplicateStudentError(f"Student {student.name} already in training")

        self.students.append(student)
