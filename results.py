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

DEFAULT_SUBJECTS = ["English", "Mathematics", "Physics", "Chemistry", "Biology"]


def validate_score(value):
    """Turn text into a number between 0 and 100, or raise ValueError."""
    score = float(value)
    if score < 0 or score > 100:
        raise ValueError("Score must be between 0 and 100.")
    return score

def class_statistics(students):
    """students is a list of Student objects. Returns a dictionary, or None."""
    graded = []
    for s in students:
        if len(s.scores) > 0:
            graded.append(s)

    if len(graded) == 0:
        return None

    averages = [s.average() for s in graded]
    all_scores = []
    for s in graded:
        all_scores.extend(s.scores.values())

    best = max(graded, key=lambda s: s.average())
    worst = min(graded, key=lambda s: s.average())

    return {
        "count": len(graded),
        "class_average": sum(averages) / len(averages),
        "top_name": best.name,
        "top_average": best.average(),
        "low_name": worst.name,
        "low_average": worst.average(),
        "highest_score": max(all_scores),
        "lowest_score": min(all_scores),
    }

# test = {"English": 80, "Maths": 75, "Physics": 90, "Chem": 65, "Bio": 70}
# print(calculate_total(test), calculate_average(test), assign_grade(calculate_average(test)))