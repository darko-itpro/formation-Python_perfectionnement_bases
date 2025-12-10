def load_students_list():
    return ['Agnan', 'Alceste', 'Clotaire', 'Eudes', 'Geoffroy', 'Joachim', 'Maixent', 'Nicolas', 'Rufus']

def load_grades(course:str):
    if course == "math":
        return [20, 15, 2, 17, 15, 6, 9, 12, 14]
    elif course == "english":
        return [19, 14, 3, 15, 8, 12, 13, 14, 16]
    else:
        raise ValueError("No course found")

def get_courses():
    return ["math", "english"]

if __name__ == '__main__':
    from pprint import pprint

    pprint(
        {name: grades
         for name, *grades in zip(load_students_list(),
                                        *[load_grades(course) for course in get_courses()],
                                        )}
    )
