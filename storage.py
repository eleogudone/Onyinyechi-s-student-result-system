

import json
import os
from student import Student

DATA_FILE = os.path.join("data","students.json")

def load_students():
    try:
        with open(DATA_FILE, "r") as file:
            raw = json.load(file)
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError:
        print("Data file is damaged. Starting fresh.")
        return {}
    else:
        return {item["student_id"]: Student.from_dict(item) for item in raw}

def save_students(students):
    try: 
        os.makedirs("data", exist_ok=True)
        with open(DATA_FILE, "w") as file:
            json.dump([s.to_dict() for s in students.values()], file, indent=4)
    except OSError as error:
        print ("Print not save:", error)
    else:
        print("Data saved.")
    finally:
        print("Save finished.")


# students = {"STU001": Student("STU001", "Ada Obi", "SS2", "F", "2008-05-21")}
# students["STU001"].set_score("English", 80)
# save_students(students)
# print(load_students()["STU001"].scores)