class Training:
    def __init__(self, subject:str, duration:int):
        self.subject = subject.title()
        self.duration = duration
        self.students = []

    def add_student(self, name:str):
        if name in self.students:
            raise ValueError(f"Student {name} already exists")

        self.students.append(name)
