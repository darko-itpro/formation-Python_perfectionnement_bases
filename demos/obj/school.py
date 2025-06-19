class Training:
    def __init__(self, subject:str, duration:int, seats:int=12):
        self.subject = subject.title()
        self.duration = int(duration)
        self.students = []
        self.seats = int(seats)

        if duration < 1:
            raise ValueError("duration must be positive")


    def __str__(self):
        return f'Training "{self.subject}" with {self.seats} seats.'

    def __repr__(self):
        return f'Training({self.subject}, {self.duration}, {self.seats})'

    def add_student(self, name):
        self.students.append(name)
