MIN_SUBJECTS = 5
def calculate_total(scores):
    return sum(scores.values())
def calculate_average(scores):
    if len(scores) == 0:
        return 0.0
    return calculate_total(scores) / len(scores)
def assign_grade(average):
    if average >= 70:
        return "A"
    elif average >= 60:
        return "B"
    elif average >= 50:
        return "C"
    elif average >= 40:
        return "D"
    else:
        return "F"

# test = {"English": 80, "Maths": 75, "Physics": 90, "Chem": 65, "Bio": 70}
# print(calculate_total(test), calculate_average(test), assign_grade(calculate_average(test)))