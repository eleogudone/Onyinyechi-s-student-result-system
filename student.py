from datetime import datetime
import results

class Student:
    def __init__(self, student_id, name, class_name, gender, dob):
        self.student_id = student_id
        self.name = name
        self.class_name = class_name
        self.gender = gender
        self.dob = dob
        self.scores = {}
        self.date_entered = None
    def set_score(self, subject, score):
        self.scores[subject] = score
        self.date_entered = datetime.now().strftime("%d-%m-%Y %H:%M")

    def total(self):
        return results.calculate_total(self.scores)
    def average(self):
        return results.calculate_average(self.scores)
    def grade(self):
        return results.assign_grade(self.average())
    def __str__(self):
        return f"{self.student_id} | {self.name} | {self.class_name}"

import re

def is_valid_id(student_id):
    return bool(re.match(r"^STU\d{3,4}$", student_id))

# s = Student("STU001", "Ada Obi", "SS2", "F", "2008-05-21")
# s.set_score("English", 80)
# s.set_score("Maths", 70)
# print(s, s.total(), s.average(), s.grade(), s.date_entered)