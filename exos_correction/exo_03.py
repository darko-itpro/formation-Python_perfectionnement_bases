from pprint import pprint
from pylib.datasources import pyacademy

def display_grades():
    print("Name       | math | English")
    for name, math_grade, english_grade in zip(pyacademy.load_students_list(),
                                               pyacademy.load_grades("math"),
                                               pyacademy.load_grades("english")):

        print("{:10} | {:4} | {:4}".format(name, math_grade, english_grade))


def get_grades():
    return {name: (math_grade, english_grade)
            for name, math_grade, english_grade in zip(pyacademy.load_students_list(),
                                                       pyacademy.load_grades("math"),
                                                       pyacademy.load_grades("english"))
            }

display_grades()
pprint(get_grades())
