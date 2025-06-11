from pylib.datasources import pyacademy as pa

for name, grade_m, grade_e in zip(pa.load_students_list(),
                                  pa.load_grades("math"),
                                  pa.load_grades("english"), ):
    print(name, grade_m, grade_e)

print(
    {name: (grade_m, grade_e)
     for name, grade_m, grade_e in zip(pa.load_students_list(),
                                       pa.load_grades("math"),
                                       pa.load_grades("english"), )}
)
