class Training:
    def __init__(self, subject: str, duration: int, seats: int = 12):
        self.subject: str = subject.title()
        self.duration = duration
        self.seats = seats
        self.students = []

    def add_student(self, name: str):
        if len(self.students) >= self.seats:
            raise ValueError('Training full')

        self.students.append(name)

    def has_seats_left(self):
        return self.seats - len(self.students) > 0