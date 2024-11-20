from pprint import pprint
import pylib.datasources.pyacademy as academy

result = {name: (math, english)
          for name, math, english in zip(academy.load_students_list(), academy.load_grades("math"),
                                         academy.load_grades("english"))}

pprint(result)
