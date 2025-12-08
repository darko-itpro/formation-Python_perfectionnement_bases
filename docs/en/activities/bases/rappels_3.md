# Iterations

For this activity, you will need the `pylib.datasources.pyacademy` module from the 
[pyschool-lib](https://github.com/darko-itpro/pyschool-lib) package. It contains two functions: 
`load_students_list()` and `load_grades(course:str)`.

 * `load_students_list()` returns a list of students
 * `load_grades(course:str)` takes one parameter between `math` or `english` and returns the list 
of marks for this subject. Any other argument will raise an exception.

It is assumed that the functions return the data in the same order (a mark in position 
i in the returned list from `load_grades(course:str)` belongs to the student in position i in the 
returned list from `load_students_list()`).

Iterate over the three collections (students, maths grades and English grades) to display the 
students with their grades.

Build a dictionary where the key is the student's name and the value is the list of their 
grades (maths in first position, English in second). Or a dictionary instead of a list.
