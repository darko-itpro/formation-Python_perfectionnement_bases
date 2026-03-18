class Training:
    def __init__(self, name:str, duration:int, seats:int = 12):
        self.subject = name.title()
        self.students = []
        self.duration = int(duration)
        self.max_seats = seats

        if self.duration < 1:
            raise ValueError(f"Duration must at least 1, got {self.duration}")

    def add_student(self, name:str):
        if self.max_seats <= len(self.students):
            raise ValueError('Training full')
        self.students.append(name)
