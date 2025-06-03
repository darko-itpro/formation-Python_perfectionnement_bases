class Student:
    def __init__(self, name, last_name, company_name):
        self.name = name
        self.last_name = last_name
        self.company_name = company_name


class TrainingSession:
    def __init__(self, subject: str, duration: int, max_seats: int):
        self.subject = subject
        self.duration = duration
        self.students = []
        self.max_seats = None

        if self.duration < 1:
            raise ValueError(f"Training duration must be greater than or equal to 1, got {self.duration}")


    def add_student(self, student: Student):
        self.students.append(student)
