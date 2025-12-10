def load_students_list():
    return ['Agnan', 'Alceste', 'Clotaire', 'Eudes', 'Geoffroy', 'Joachim', 'Maixent', 'Nicolas', 'Rufus']

def load_grades(course:str):
    if course == "math":
        return [20, 15, 2, 17, 15, 6, 9, 12, 14]
    elif course == "english":
        return [19, 14, 3, 15, 8, 12, 13, 14, 16]
    else:
        raise ValueError("No course found")

if __name__ == '__main__':
    from pprint import pprint

    pprint(
        {name: {"math":math, "english":english}
         for name, math, english in zip(load_students_list(),
                                        load_grades('math'),
                                        load_grades('english'))}
    )
