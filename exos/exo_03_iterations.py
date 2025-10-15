import pylib.datasources.pyacademy as academy
from pprint import pprint

pprint(
    {name: {"math": math, "english": english}
     for name, math, english in zip(academy.load_students_list(),
                                    academy.load_grades('math'),
                                    academy.load_grades('english'),
                                    )
     }
)
