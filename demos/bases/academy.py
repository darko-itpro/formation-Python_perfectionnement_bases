class Training:
    def __init__(self, name:str, duration:int, seats:int = 12):
        self.subject = name
        self._students = []
        self.duration = int(duration)
        self.max_seats = seats

        if self.duration < 1:
            raise ValueError(f"Duration must at least 1, got {self.duration}")

    @property
    def available_seats(self):
        return self.max_seats - len(self._students)

    @property
    def subject(self):
        return self._subject

    @subject.setter
    def subject(self, new_subject:str):
        self._subject = new_subject.title()

    @property
    def students(self):
        return self._students.copy()

    def add_student(self, name:str):
        if self.max_seats <= len(self.students):
            raise ValueError('Training full')
        self.students.append(name)
