import pylib.datasources.pyacademy as pa

print("script starded")

grades = {name: [math_grade, english_grade]
          for name, math_grade, english_grade in zip(pa.load_students_list(),
                                                     pa.load_grades("math"),
                                                     pa.load_grades("english"))}

print(grades)
