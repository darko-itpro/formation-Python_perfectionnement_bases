from pylib.datasources import pyacademy

for name, math, english in zip(
        pyacademy.load_students_list(),
        pyacademy.load_grades("math"),
        pyacademy.load_grades("english")):
    print(f"{name:^10} | {math:4} | {english:4}")

grades = {name: {"math": math, "english": english}
          for name, math, english in zip(
        pyacademy.load_students_list(),
        pyacademy.load_grades("math"),
        pyacademy.load_grades("english"))}

print(grades)
