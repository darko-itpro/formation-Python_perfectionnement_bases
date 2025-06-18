from pprint import pprint
from pylib.datasources import pyacademy

pyacademy.load_students_list()
pyacademy.load_grades("math")
pyacademy.load_grades("english")

print("Première question")

print("   name    |    math    |   english")

for student, math, english in zip(pyacademy.load_students_list(),
                                  pyacademy.load_grades("math"),
                                  pyacademy.load_grades("english"),):
    print("{:10} | {:10} | {:10}".format(student, math, english))

print()
print("Seconde question")

pprint(
    {student: {"math": math, "englilsh": english}
     for student, math, english in zip(pyacademy.load_students_list(),
                                       pyacademy.load_grades("math"),
                                       pyacademy.load_grades("english"), )}
)
