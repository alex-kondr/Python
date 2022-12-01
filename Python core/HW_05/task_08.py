grades = {"A": 5, "B": 5, "C": 4, "D": 3, "E": 3, "FX": 2, "F": 1}

def formatted_grades(students):

    list = []
    number = 1

    for name, grade_ECTS in students.items():

        grade = grades[grade_ECTS]
        list.append("{:>4}|{:<10}|{:^5}|{:^5}".format(number, name, grade_ECTS, grade))
        number += 1

    return list
