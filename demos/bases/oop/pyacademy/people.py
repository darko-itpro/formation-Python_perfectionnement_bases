
from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self, first_name: str, last_name: str, id:str):
        self.first_name = first_name
        self.last_name = last_name
        self.id = id

    @abstractmethod
    def calculate_payroll(self):
        pass

class Student:
    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f"Student {self.first_name}, {self.last_name}"

    def __repr__(self):
        return self.__str__()

class SalaryEmployee(Employee):
    def __init__(self, first_name, last_name, id, monthly_salaray):
        super().__init__(first_name, last_name, id)
        self.monthly_salaray = monthly_salaray

    def calculate_payroll(self):
        return self.monthly_salaray

class DailyEmployee(Employee):
    def __init__(self, first_name, last_name, id, daily_rate):
        super().__init__(first_name, last_name, id)
        self.daily_rate = daily_rate
        self.days = 0

    def work(self, days):
        self.days += days

    def calculate_payroll(self):
        return self.days * self.daily_rate


se = SalaryEmployee("John", "Doe", "id", 2500)
print(se.calculate_payroll())

de = DailyEmployee("Bobba", "Fett", "42", 500)
de.work(5)
de.work(2)
print(de.calculate_payroll())


class SalesEmployee:
    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f"Coach {self.first_name}, {self.last_name}"

    def __repr__(self):
        return self.__str__()

    def add_student_to(self, student, training):
        training.add_student(student)


class Coach(SalaryEmployee):
    pass

class DailyCoach(Coach, DailyEmployee):
    def __init__(self, first_name, last_name, id, daily_rate):
        DailyEmployee.__init__(self, first_name, last_name, id, daily_rate)

    def __str__(self):
        return f"Coach {self.first_name}, {self.last_name}"

    def __repr__(self):
        return self.__str__()
#e = DailyCoach("John", "Doe", 52, 800)
#e.days = 10
#print(e.calculate_payroll())

class MyMetaClasse(type):
    def __call__(self, *argv, **kwargs):
        print("Dans call METACLASSE")
        return super().__call__(*argv, **kwargs)

    def __new__(cls, name, base, dct):
        print("Dans new METACLASSE")
        return super().__new__(cls, name, base, dct)

    def __init__(self, *argv, **kwargs):
        print("Dans init METACLASSE")
        super().__init__(*argv, **kwargs)

class MyClass(metaclass=MyMetaClasse):
    pass