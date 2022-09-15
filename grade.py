def get_grade(key):

    ECTS_to_rating = {
        "F": 1, 
        "FX": 2, 
        "E": 3, 
        "D": 3,
        "C": 4,
        "B": 5,
        "A": 5
    }

    return ECTS_to_rating.get(key)

def get_description(key):
    
    ECTS_to_explanation = {
        "F": "Unsatisfactorily",
        "FX": "Unsatisfactorily",
        "E": "Enough",
        "D": "Satisfactorily",
        "C": "Good",
        "B": "Very good",
        "A": "Perfectly"
    }

    return ECTS_to_explanation.get(key)
